import pandas as pd
import psycopg2
from psycopg2.extras import RealDictCursor
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from neo4j import GraphDatabase
import os
import traceback
import requests
from tabulate import tabulate
from query_generation.Prompt import TIME_SCALE_DB_CONTEXT
import re

class RAGQueryGenerator:
    def __init__(self, neo4j_uri, neo4j_username, neo4j_password,
                 pg_host, pg_database, pg_user, pg_password,
                 top_k=2, bfs_depth=3):
        
        # Initialize Neo4j connection
        self.driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_username, neo4j_password))
        
        # Initialize Postgres connection parameters
        self.pg_host = pg_host
        self.pg_database = pg_database
        self.pg_user = pg_user
        self.pg_password = pg_password

        # Load the embedding model
        self.encoder = SentenceTransformer("paraphrase-mpnet-base-v2")
        # FAISS parameters
        self.top_k = top_k
        self.bfs_depth = bfs_depth
        self.index = None  # To be built after loading schema data
        self.schema_df = None
        # Mappings for quick lookup: id -> text and other info.
        self.id_to_text = {}
        self.id_to_info = {}

        self.context = None
        self.table_name = None


    def fetch_schema_from_postgres(self, conn):
        """
        Connects to PostgreSQL and retrieves table names, columns, and foreign key relationships.
        The schema data is stored in a DataFrame. Each row represents a table.
        """

        # conn = psycopg2.connect(
        #     dbname=self.pg_database,
        #     user=self.pg_user,
        #     password=self.pg_password,
        #     host=self.pg_host,
        #     port=""
        # )

        cursor = conn.cursor(cursor_factory=RealDictCursor)
    
        # Query to get tables and their columns from the public schema.
        table_query = """
        SELECT table_name
        FROM information_schema.tables 
        WHERE table_schema = 'public' AND table_type = 'BASE TABLE';
        """
        cursor.execute(table_query)
        tables = cursor.fetchall()

        data = []
        table_id = 0
        for table in tables:
            table_name = table['table_name']
            # Get columns for this table.
            cursor.execute("""
                SELECT column_name
                FROM information_schema.columns
                WHERE table_schema = 'public' AND table_name = %s;
            """, (table_name,))

            cursor.execute("""
                SELECT column_name, data_type
                FROM information_schema.columns
                WHERE table_schema = 'public' AND table_name = %s;
            """, (table_name,))
            columns = cursor.fetchall()
            col_names = ", ".join([f"{col['column_name']} ({col['data_type']})" for col in columns])

            # columns = cursor.fetchall()
            # col_names = ", ".join([col['column_name'] for col in columns])
            # Create a text representation.
            text = f"Table: {table_name}. Columns: {col_names}."
            data.append([table_id, table_name, col_names, text])
            table_id += 1

        # Create DataFrame for tables
        df = pd.DataFrame(data, columns=['id', 'table_name', 'columns', 'text'])

                     # --- Fetch TimescaleDB hypertable information ---
        hypertable_query = """
        SELECT hypertable_name
        FROM timescaledb_information.hypertables;
        """
        cursor.execute(hypertable_query)
        hypertables = cursor.fetchall()
        
        # Create a set of hypertable names for quick lookup
        ht_names = { ht['hypertable_name'] for ht in hypertables }
        
        # Update the text representation for each table based on hypertable info.
        def append_hypertable_info(row):
            if row['table_name'] in ht_names:
                # If you want to also show the time column, you could modify this if you have that info.
                return row['text'] + " [Hypertable: Yes]"
            else:
                return row['text'] + " [Hypertable: No]"
        
        df['text'] = df.apply(append_hypertable_info, axis=1)

 
        # Query to get foreign key relationships.
        fk_query = """
        SELECT tc.table_name as source_table, 
               kcu.column_name as source_column,
               ccu.table_name as target_table,
               ccu.column_name as target_column
        FROM information_schema.table_constraints AS tc 
        JOIN information_schema.key_column_usage AS kcu
          ON tc.constraint_name = kcu.constraint_name
          AND tc.table_schema = kcu.table_schema
        JOIN information_schema.constraint_column_usage AS ccu
          ON ccu.constraint_name = tc.constraint_name
          AND ccu.table_schema = tc.table_schema
        WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_schema = 'public';
        """
        cursor.execute(fk_query)
        fks = cursor.fetchall()
        # Store foreign key relationships in the DataFrame for later use.
        # Here we add a column with a list of target tables for each source table.
        df['fk_targets'] = [[] for _ in range(len(df))]
        for fk in fks:
            source = fk['source_table']
            target = fk['target_table']
            # Find the corresponding table ids in df.
            source_id = df[df['table_name'] == source]['id']
            target_id = df[df['table_name'] == target]['id']
            if not source_id.empty and not target_id.empty:
                src_id = int(source_id.iloc[0])
                tgt_id = int(target_id.iloc[0])
                df.at[src_id, 'fk_targets'].append(tgt_id)
        # cursor.close()
        # conn.close()

        self.schema_df = df

        # Build mapping dictionaries
        self.id_to_text = df.set_index('id')['text'].to_dict()
        self.id_to_info = df.set_index('id').to_dict(orient='index')
        print("Fetched schema from Postgres:")
        print(df[['id', 'table_name', 'columns', 'fk_targets']])

    def build_faiss_index(self):
        """
        Encodes the schema text using the SentenceTransformer and builds a FAISS index.
        """

        texts = self.schema_df['text'].tolist()
        embeddings = self.encoder.encode(texts, show_progress_bar=True)
        faiss.normalize_L2(embeddings)
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)

        print("FAISS index built with schema embeddings.")

    def create_schema_graph(self):
        """
        Creates nodes in Neo4j for each table from the schema and adds relationships based on foreign keys.
        """
        with self.driver.session() as session:
            # Clear previous graph data
            session.run("MATCH (n) DETACH DELETE n")
            # Create nodes for each table
            for _, row in self.schema_df.iterrows():
                session.run(
                    "CREATE (:Table {id: $id, table_name: $table_name, columns: $columns, text: $text})",
                    {"id": int(row['id']),
                     "table_name": row['table_name'],
                     "columns": row['columns'],
                     "text": row['text']
                     }
                )
            # Create relationships based on foreign keys
            for _, row in self.schema_df.iterrows():
                source_id = int(row['id'])
                # For each target id in the fk_targets list, create a relationship.
                for target_id in row['fk_targets']:
                    session.run("""
                        MATCH (a:Table {id: $src}), (b:Table {id: $dst})
                        CREATE (a)-[:FK_TO]->(b)
                    """, {"src": source_id, "dst": target_id})

                    session.run("""
                        MATCH (a:Table {id: $dst}), (b:Table {id: $src})
                        CREATE (a)-[:FK_TO]->(b)
                    """, {"src": source_id, "dst": target_id})

            print("Neo4j schema graph created. You can view it in the browser with:")
            print("MATCH (n)-[r:FK_TO]->(m) RETURN n, r, m")


    def search_context(self, prompt):
        """
        Given a natural language prompt, this method:
        1. Encodes the prompt and retrieves the top_k FAISS matches.
        2. For each match, it queries Neo4j to retrieve related nodes up to bfs_depth.
        3. Aggregates the schema information from FAISS and BFS to form a context string.
        4. Collects all relevant table names used in context.
        
        Returns:
            (context_string, comma-separated list of table names)
        """
        # Encode the prompt
        query_vector = self.encoder.encode([prompt])
        faiss.normalize_L2(query_vector)
        distances, ann = self.index.search(query_vector, k=self.top_k)

        context_lines = []
        context_lines.append("Top FAISS Matches:")
        table_names_set = set()

        for idx, dist in zip(ann[0], distances[0]):
            id_val = self.schema_df.iloc[idx]['id']
            info = self.id_to_info[id_val]

            context_lines.append(
                f"ID: {id_val}, Table Name: {info['table_name']}, Column Names: {info['columns']} (distance: {dist:.4f})"
            )

            table_names_set.add(info['table_name'])

        # BFS context from Neo4j
        with self.driver.session() as session:
            for idx in ann[0]:
                node_id = int(self.schema_df.iloc[idx]['id'])
                bfs_context = self.get_bfs_context(session, node_id, depth=self.bfs_depth)
                context_lines.append(f"\nContext for Table ID {node_id}:")
                if bfs_context:
                    for entry in bfs_context:
                        context_lines.append(f"  -> {entry}")
                        match = re.search(r"Table(?: Name)?: (\w+)", entry)
                        if match:
                            table_names_set.add(match.group(1))
                else:
                    context_lines.append("  No additional context found.")

        table_names_str = ", ".join(sorted(table_names_set))
        return "\n".join(context_lines), table_names_str


    def get_bfs_context(self, session, node_id, depth=1):
        """
        Query Neo4j to retrieve nodes connected to the given node (by FK_TO relationships) up to the specified depth.
        Returns a list of strings describing each connected node.
        """
        query = f"""
        MATCH (n:Table {{id: $node_id}})-[:FK_TO*1..{depth}]->(neighbor)
        RETURN DISTINCT neighbor.id AS id, neighbor.table_name AS table_name, neighbor.columns AS columns
        """
        results = session.run(query, node_id=node_id)
        return [f"ID: {r['id']}, Table Name: {r['table_name']}, Columns: {r['columns']}" for r in results]

 
    def generate_llm_prompt(self, user_prompt: str) -> str:
        """
        Generates a highly structured prompt for SQL query generation from natural language
        using best practices for LLMs .

        Args:
            user_prompt: Natural language query for SQL.

        Returns:
            Formatted prompt string.
        """

        self.context, self.table_name = self.search_context(user_prompt)

        llm_prompt = f"""You are an expert SQL query generator. But I want you to generate queries for a TimeScaleDB, a system which is an optimised version of postgres for time series data. You can also use normal postgres sql syntax for queries to solve the user prompts. But as this is TimeScale DB, 
        but using TimeScaleDB operations optimise certain operations leading to faster query processing. Hence make sure to try and use TimeScaleDB operations whenever possible and required to save the user's time.

        {TIME_SCALE_DB_CONTEXT}

        Given a User question given below and a relational database schema Context in the TimeScale DB environment, your task is to write a valid SQL query
        that runs without syntax errors in the TimeScaleDB environment with the Schemas in "Database Schema Context" given below. The schema includes relationships across multiple tables.

        User Question:
        {user_prompt}

        Database Schema Context:
        {self.context}

        Instructions:
        - You can only use table names from the following list:
            {self.table_name}
        - Use only table names and column names that are present in the database according to the "Database Schema Context".
        - Use JOINs where necessary to connect tables.
        - Include all relevant attributes required to fulfill the user prompt.
        - Avoid unnecessary columns.
        - If any filtering, ordering, or aggregation is relevant, include it in the query.
        
        Perform the following actions step by step:
        1. Understand the table names the column names for each of these table names from Database Schema Context to use in the TimeScale DB query.
        2. Generate a TimeScale DB Query.
        3. Check if you have used any table names not in the Database Schema Context.
        4. If any table is not present, generate another query and go to the previous action.
        5. Now Check if the column names in all tables are present in Database Schema Context.
        6. If some columns are not present, generate another query and check it in the above fashion.
        7. Finally generate a query that will surely run "WITHOUT SYNTAX ERROR" in the system with the Schemas present in Database Schema Context.
        8. If you are not sure, again generate a query and make sure it runs in the system.

        --- SQL Query ---
        """

        return llm_prompt
    
    def retry_llm_prompt(self, query, error):
        """
            prompt when the query is wrong
        """
        
        llm_prompt = f"""You are an expert SQL query generator.

        Your previous prompt was wrong. You gave given in QUERY section below. That gave the error given in ERROR section below the QUERY section.
        
        User Question:
        {user_prompt}

        QUERY:
        {query}

        ERROR:
        {error}

        We are giving you another chance to correct your mistake. The Database Schema Context contains the table names and column names in the database you are going to query.
        Your task is to generate an sql query that runs without syntax errors in the given database. Make sure to follow all the instructions given in instructions section. 

        Database Schema Context:
        {self.context}

        Instructions:
        - You can only use table names from the following list:
            {self.table_name}
        - Use only table names and column names that are present in the database according to the "Database Schema Context".
        - Use JOINs where necessary to connect tables.
        - Include all relevant attributes required to fulfill the user prompt.
        - Avoid unnecessary columns.
        - If any filtering, ordering, or aggregation is relevant, include it in the query.
        
        Perform the following actions step by step:
        1. Understand the table names the column names for each of these table names from Database Schema Context to use in the sql query.
        2. Generate an Sql Query.
        3. Check if you have used any table names not in the Database Schema Context.
        4. If any table is not present, generate another query and go to the previous action.
        5. Now Check if the column names in all tables are present in Database Schema Context.
        6. If some columns are not present, generate another query and check it in the above fashion.
        7. Finally generate a query that will surely run "WITHOUT SYNTAX ERROR" in the system with the Schemas present in Database Schema Context.
        8. If you are not sure, again generate a query and make sure it runs in the system.

        --- SQL Query ---
        """

        return llm_prompt
    
    def run_sql_query(self, sql_query):
        """
        Executes the given SQL query on a PostgreSQL database.
        """
 
        conn = psycopg2.connect(
            dbname=self.pg_database,
            user=self.pg_user,
            password=self.pg_password,
            host=self.pg_host,
            port=""
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(sql_query)
            
            # If it's a SELECT query
            if sql_query.strip().lower().startswith("select"):
                rows = cur.fetchall()
                # colnames = [desc[0] for desc in cur.description]
                # result = [dict(zip(colnames, row)) for row in rows]

                data = []
                for row in rows:
                    data.append(dict(row))
                cur.close()
                conn.close()
                return data, None

            # For INSERT/UPDATE/DELETE
            conn.commit()
            cur.close()
            conn.close()
            return {"status": "success"}, None
        except:
            error_trace = traceback.format_exc()

            return None, error_trace

# Call gemini api to get data output
def query_gemini(prompt, max_tokens=300, temperature=0.7):

    # Set your API key and endpoint.
    API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key=" + API_KEY
    
    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        "model":"gemini-1.5-pro",
        "contents": [
        {
            "parts": [
            {
                "text": f"You are an expert SQL query generator and must use table names exactly as provided in the schema context. \n\nSolve the given problem accurately.\n{prompt}"
            }
            ]
        }
        ]
    }

    response = requests.post(GEMINI_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        # Extract content; adjust extraction based on actual response format.
        try:
            generated_text = result['candidates'][0]['content']['parts'][0]['text']
            return generated_text.strip()
        except (KeyError, IndexError) as e:
            print("Error extracting response:", e)
            return None
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")
        return None



# parse out the sql query
def extract_sql_query(response_text: str) -> str:
    """
    Extracts SQL code from a markdown code block labeled with ```sql.
    """
    match = re.search(r"```sql(.*?)```", response_text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    raise ValueError("No SQL code block found in the response.")


# -------------------------
# Example Usage
# -------------------------
if __name__ == "__main__":
    # Initialize our RAG query generator with Neo4j and Postgres connection parameters.
    rag = RAGQueryGenerator(
        neo4j_uri="bolt://localhost:7687",
        neo4j_username="neo4j",
        neo4j_password="vishwa2488",
        pg_host="10.102.75.119",
        pg_database="timeseries",
        pg_user="postgres",
        pg_password="secret",
        top_k=2,
        bfs_depth=3
    )

    # Fetch the schema directly from Postgres and build the FAISS index.
    rag.fetch_schema_from_postgres()
    rag.build_faiss_index()

    # Create the knowledge graph in Neo4j from the fetched schema.
    rag.create_schema_graph()
    
    # Now, generate a prompt for SQL query generation based on a natural language request.
    user_prompt = "Give the average load in truck over every 2 second bucket."


    llm_prompt = rag.generate_llm_prompt(user_prompt)
    print("\n--- LLM Prompt ---")
    print(llm_prompt)

    result = query_gemini(llm_prompt)
    print("Output:")
    print(result)

    sql_query = extract_sql_query(result)

    print(f"SQL Query:\n{sql_query}")

    final_output, error = rag.run_sql_query(sql_query)

    if (final_output == None):
        
        print("Error Trace:")
        print(error)
        llm_prompt = rag.retry_llm_prompt(sql_query, error)
        result = query_gemini(llm_prompt)
        print(result)

    elif isinstance(final_output, list):
        print(tabulate(final_output, headers="keys", tablefmt="grid"))
    elif isinstance(final_output, dict):
        print(final_output)
    else:
        print("output_unknown format\n")
        print(final_output)
        




 




