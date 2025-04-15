#!/usr/bin/env python3
"""
Direct implementation of Balsa plan optimization without depending on Balsa's infrastructure.
"""
import os
import sys
import psycopg2
import json
import torch
import time
from query_generation.DatabaseQueryRAG import RAGQueryGenerator, query_gemini, extract_sql_query

def connect_to_db():
    """Connect to the TimescaleDB database."""
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="timescaledb_test",
            user="postgres",
            password="postgres"
        )
        print("Connected to TimescaleDB")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)

def get_pg_plan(conn, sql):
    """Get PostgreSQL's plan for a query."""
    with conn.cursor() as cursor:
        cursor.execute(f"EXPLAIN (FORMAT JSON) {sql}")
        plan = cursor.fetchone()[0]
    return plan

def execute_query(conn, sql, hint=None):
    """Execute a query and measure the time."""
    try:
        query = sql
        if hint:
            query = f"{hint}\n{sql}"
        
        with conn.cursor() as cursor:
            start = time.time()
            cursor.execute("EXPLAIN (ANALYZE, FORMAT JSON) " + query)
            result = cursor.fetchone()[0]
            end = time.time()
            query_result = cursor.execute(query)
            query_result = cursor.fetchall()
            print(f"Query Result : {query_result}")
            
            # Extract execution time from the result
            exec_time = result[0]['Execution Time']
            return exec_time, result
    except Exception as e:
        print(f"Error executing query: {e}")
        return None, None
    
def get_join_orders_from_pg_plan(plan_json):
    """Extract all joins from the PostgreSQL plan."""
    joins = []
    
    def extract_joins(node, path=[]):
        if 'Plans' not in node:
            # Leaf node - likely a scan
            table_name = None
            if 'Relation Name' in node:
                table_name = node['Relation Name']
            elif 'Alias' in node:
                table_name = node['Alias']
                
            if table_name:
                path.append(table_name)
                return [table_name]
            return []
            
        # Non-leaf node
        if 'Join Type' in node:
            # This is a join node
            left_tables = []
            right_tables = []
            
            if len(node['Plans']) >= 2:
                left_tables = extract_joins(node['Plans'][0], path + ['left'])
                right_tables = extract_joins(node['Plans'][1], path + ['right'])
                
            join_info = {
                'join_type': node['Join Type'],
                'left': left_tables,
                'right': right_tables
            }
            joins.append(join_info)
            return left_tables + right_tables
        else:
            # Not a join - recurse into children
            all_tables = []
            for child in node['Plans']:
                all_tables.extend(extract_joins(child, path + ['child']))
            return all_tables
    
    # Start extraction from the root
    extract_joins(plan_json[0]['Plan'])
    return joins

def generate_hint_string(join_orders):
    """Generate a hint string based on join order."""
    hint = "/*+"
    
    # Add join order hints
    for i, join in enumerate(join_orders):
        left_tables = join['left']
        right_tables = join['right']
        
        if left_tables and right_tables:
            if join['join_type'] == 'Hash Join':
                hint += f" HashJoin({', '.join(left_tables)} {', '.join(right_tables)})"
            elif join['join_type'] == 'Merge Join':
                hint += f" MergeJoin({', '.join(left_tables)} {', '.join(right_tables)})"
            elif join['join_type'] == 'Nested Loop':
                hint += f" NestedLoop({', '.join(left_tables)} {', '.join(right_tables)})"
            else:
                hint += f" Leading({', '.join(left_tables + right_tables)})"
    
    hint += " */"
    return hint

def main():
    # Connect to the database
    conn = connect_to_db()
    
    rag = RAGQueryGenerator(
        neo4j_uri="bolt://localhost:7687",
        neo4j_username="neo4j",
        neo4j_password="swamiallen@123",
        pg_host="10.102.75.119",
        pg_database="timeseries",
        pg_user="postgres",
        pg_password="secret",
        top_k=2,
        bfs_depth=3
    )

    # Fetch the schema directly from Postgres and build the FAISS index.
    rag.fetch_schema_from_postgres(conn)
    rag.build_faiss_index()

    # Create the knowledge graph in Neo4j from the fetched schema.
    rag.create_schema_graph()

    # Now, generate a prompt for SQL query generation based on a natural language request.
    user_prompt = f"""Generate a SQL query to calculate hourly averages of temperature."""
    llm_prompt = rag.generate_llm_prompt(user_prompt)
    print("\n--- LLM Prompt ---")
    print(llm_prompt)

    result = query_gemini(llm_prompt)

    sql_query = extract_sql_query(result)

    sql_query = sql_query.split(";")[0] # NOTE: For now just use the first query
    print("Output:")
    print(result)

    # Read the SQL query
    # try:
    #     with open('custom_timeseries_query.sql', 'r') as f:
    #         sql = f.read().strip()
    #     print(f"Read SQL query ({len(sql)} characters)")
    # except Exception as e:
    #     print(f"Error reading SQL file: {e}")
    #     sys.exit(1)
    
    # Get PostgreSQL's plan
    pg_plan = get_pg_plan(conn, sql_query)
    print("Got PostgreSQL plan")
    
    # Execute the query with the default plan
    pg_time, pg_execution = execute_query(conn, sql_query)
    print(f"Default PostgreSQL execution time: {pg_time} ms")
    
    # Extract joins from the plan
    joins = get_join_orders_from_pg_plan(pg_plan)
    print(f"Extracted {len(joins)} joins from the plan")
    
    # Generate a hint string
    # Here we're just using PostgreSQL's plan for demonstration
    # In practice, Balsa would generate a different plan
    hint = generate_hint_string(joins)
    print("Generated hint string:")
    print(hint)
    
    # Execute with the hint
    hint_time, hint_execution = execute_query(conn, sql_query, hint)
    print(f"Execution time with hint: {hint_time} ms")
    
    # Compare times
    if pg_time and hint_time:
        improvement = (pg_time - hint_time) / pg_time * 100
        print(f"\nPerformance comparison:")
        print(f"  Default PostgreSQL:  {pg_time:.2f} ms")
        print(f"  With hint:           {hint_time:.2f} ms")
        print(f"  Improvement:         {improvement:.2f}% ({'better' if improvement > 0 else 'worse'})")
    
    # Close connection
    conn.close()

if __name__ == "__main__":
    main()
