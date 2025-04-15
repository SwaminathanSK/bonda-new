#!/usr/bin/env python3

import rospy
import psycopg2
import psycopg2.extras # For execute_batch
import threading
from datetime import datetime
import importlib # To dynamically import message types
import json

# --- Configuration (Loaded from ROS Param Server) ---
# Database connection
DB_HOST = ""
DB_PORT = 5432
DB_NAME = ""
DB_USER = ""
DB_PASSWORD = ""
# Topic details
TOPIC_NAME = ""
# Message type needs package/MsgName format, e.g., "sensor_msgs/Imu"
TOPIC_MSG_TYPE_STR = ""
# Ingestion details
DB_TABLE_NAME = ""
# Mapping: { 'db_column_name': 'ros_msg_field_path' }
# Use dots for nested fields, e.g., 'header.stamp', 'linear_acceleration.x'
COLUMN_MAPPING = {}
# Batching controls
BATCH_SIZE = 100 # Number of messages to batch before inserting
FLUSH_INTERVAL_SECONDS = 5.0 # Max time between flushing batches

# --- Global Variables ---
connection = None
cursor = None
data_buffer = []
buffer_lock = threading.Lock() # To protect access to the buffer
MsgType = None # Will hold the imported message class

def get_nested_attr(obj, attr_path):
    """Safely retrieves nested attributes."""
    attrs = attr_path.split('.')
    try:
        for attr in attrs:
            if '[' in attr and attr.endswith(']'): # Handle list indices like ranges[0]
                 base_attr, index_str = attr.split('[')
                 index = int(index_str[:-1]) # Remove ']' and convert to int
                 obj = getattr(obj, base_attr)[index]
            else:
                obj = getattr(obj, attr)
        return obj
    except (AttributeError, IndexError, TypeError) as e:
        rospy.logwarn_throttle(10, f"Could not retrieve attribute '{attr_path}': {e}")
        return None # Return None if any part of the path is invalid

def connect_db():
    """Establishes connection to the TimescaleDB database."""
    global connection, cursor
    while not rospy.is_shutdown() and connection is None:
        try:
            rospy.loginfo(f"Connecting to database '{DB_NAME}' at {DB_HOST}:{DB_PORT}...")
            connection = psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
            cursor = connection.cursor()
            rospy.loginfo("Database connection successful.")
        except psycopg2.OperationalError as e:
            rospy.logerr(f"Database connection failed: {e}. Retrying in 5 seconds...")
            rospy.sleep(5.0) # Wait before retrying

def shutdown_hook():
    """Closes the database connection on node shutdown."""
    rospy.loginfo("Shutdown signal received. Flushing final buffer...")
    flush_buffer() # Ensure any remaining data is flushed
    if cursor:
        cursor.close()
        rospy.loginfo("Database cursor closed.")
    if connection:
        connection.close()
        rospy.loginfo("Database connection closed.")

def flush_buffer():
    """Inserts the buffered data into the database."""
    global data_buffer
    with buffer_lock: # Acquire lock to safely access buffer
        if not data_buffer:
            return # Nothing to flush
        # Make a copy and clear the shared buffer immediately
        buffer_copy = data_buffer[:]
        data_buffer = []
    # --- Outside the lock ---

    # --- Add this check ---
    if not buffer_copy:
        rospy.logwarn("Flush buffer called with empty buffer_copy after lock.")
        return # Nothing to insert

    try:
        columns = list(COLUMN_MAPPING.keys())
        num_columns = len(columns)
        num_values_in_first_row = len(buffer_copy[0])

        if num_columns != num_values_in_first_row:
            rospy.logerr(f"CRITICAL ERROR: Column count ({num_columns}) from COLUMN_MAPPING does not match value count in data tuple ({num_values_in_first_row})!")
            rospy.logerr(f"Columns expected ({num_columns}): {columns}")
            rospy.logerr(f"Values found in first row ({num_values_in_first_row}): {buffer_copy[0]}")
            # Consider how to handle this error - maybe clear buffer_copy?
            # For now, just returning to prevent the execute_batch error.
            return # Stop processing this broken batch
        # --- End check ---

        rospy.logdebug(f"Flushing {len(buffer_copy)} messages to table '{DB_TABLE_NAME}'. Column/Value counts match ({num_columns}).")
        # # Dynamically create column names and placeholders for the SQL query
        # sql = f"INSERT INTO {DB_TABLE_NAME} ({', '.join(columns)}) VALUES %s"

        # --- CHANGE THE SQL STRING GENERATION ---
        # Create '%s, %s, ..., %s' string based on number of columns
        placeholders = ', '.join(['%s'] * num_columns)
        # Build the SQL string with explicit placeholders for each value
        sql = f"INSERT INTO {DB_TABLE_NAME} ({', '.join(columns)}) VALUES ({placeholders})"
        # --- END SQL STRING CHANGE ---

        rospy.logdebug(f"Executing batch SQL: {sql}")
        rospy.logdebug(f"Number of rows in batch: {len(buffer_copy)}")

        # Use execute_batch for efficient bulk insertion
        psycopg2.extras.execute_batch(cursor, sql, buffer_copy)
        connection.commit()
        rospy.logdebug(f"Successfully inserted batch of {len(buffer_copy)}.")

    except psycopg2.Error as e:
        rospy.logerr(f"Database insert/commit error: {e}")
        rospy.logerr(f"Failed data batch sample (first item): {buffer_copy[0] if buffer_copy else 'N/A'}")
        if connection:
            try:
                connection.rollback()
            except psycopg2.Error as rb_e:
                 rospy.logerr(f"Rollback failed: {rb_e}")
    except Exception as e:
        # This error should hopefully be gone now, but keep the logging
        rospy.logerr(f"An unexpected error occurred during flush: {e}")
        rospy.logerr(f"Failed data batch sample (first item): {buffer_copy[0] if buffer_copy else 'N/A'}")
        rospy.logerr(f"Columns expected based on mapping: {list(COLUMN_MAPPING.keys())}")
        rospy.logerr(f"SQL attempted: {sql if 'sql' in locals() else 'SQL not generated'}") # Log the SQL

def timer_callback(event):
    """Called periodically to flush the buffer based on time."""
    # Check connection health (optional, basic check)
    if connection is None or connection.closed != 0:
        rospy.logwarn("Database connection lost. Attempting to reconnect...")
        connect_db() # Try to reconnect
        if connection is None: # If still not connected, skip flush
             return

    if len(data_buffer) > 0: # Only flush if there's data
        rospy.logdebug(f"Timer triggered flush. Buffer size: {len(data_buffer)}")
        flush_buffer()

# --- Inside message_callback function ---
def message_callback(msg):
    print("\n--- Processing new message ---") # New print
    row_data = []
    valid_row = True
    # Make sure COLUMN_MAPPING is defined globally or passed correctly
    # print(f"DEBUG: Column Mapping Used: {COLUMN_MAPPING}") # Optional: Uncomment to verify mapping

    for db_col, ros_field in COLUMN_MAPPING.items():
        print(f"Processing column: '{db_col}', ROS field: '{ros_field}'") # New print
        value = get_nested_attr(msg, ros_field)
        print(f"  Initial value fetched: {value} (type: {type(value)})") # New print

        # --- Start Enhanced Timestamp Handling ---
        if hasattr(value, 'secs') and hasattr(value, 'nsecs'):
            print(f"  Detected rospy.Time for field '{ros_field}'!") # New print
            if value.is_zero():
                print(f"  Timestamp is zero, setting value to None.") # New print
                value = None
            else:
                try:
                    value_sec = value.to_sec()
                    converted_dt = datetime.utcfromtimestamp(value_sec)
                    print(f"  Converted {value_sec} to datetime: {converted_dt}") # New print
                    value = converted_dt # The crucial reassignment
                    print(f"  Value variable AFTER conversion assignment: {value} (type: {type(value)})") # New print
                except ValueError as e:
                    print(f"  ERROR converting timestamp {value.to_sec()}: {e}. Setting value to None.") # New print
                    value = None
        # --- End Enhanced Timestamp Handling ---

        # --- Start Handling for JSONB arrays ---
        elif ros_field in ["ranges", "intensities"] and isinstance(value, (list, tuple)):
            print(f"  Detected list/tuple for JSONB field '{ros_field}'.") # New print
            try:
                value = json.dumps(value)
                print(f"  Converted list/tuple to JSON string.") # New print
            except TypeError as e:
                print(f"  ERROR converting field '{ros_field}' to JSON: {e}. Setting value to None.") # New print
                value = None
        # --- End Handling for JSONB arrays ---

        # Check for None timestamp (should happen AFTER conversion attempt)
        # Use the mapped ros_field to identify the time column
        mapped_time_fields = ['header.stamp', 'time'] # Define possible time fields
        if value is None and ros_field in mapped_time_fields:
             print(f"  WARNING: Timestamp field '{ros_field}' resolved to None. Skipping message.") # New print
             valid_row = False
             break

        print(f"  >> Appending to row_data: {value} (type: {type(value)})") # New print
        row_data.append(value)

    if valid_row:
        print(f"--- Final row_data tuple prepared: {tuple(row_data)}") # New print
        with buffer_lock:
            data_buffer.append(tuple(row_data))
            buffer_len = len(data_buffer)
            if buffer_len >= BATCH_SIZE * 1.5: # Check if significantly over size
                 print(f"--- Flushing buffer early due to size: {buffer_len}") # New print
                 flush_buffer()
    else:
        print("--- Message skipped due to invalid row (likely None timestamp).") # New print


def import_message_type(type_str):
    """Dynamically imports the ROS message class from string."""
    try:
        pkg_name, msg_name = type_str.split('/')
        module = importlib.import_module(pkg_name + '.msg')
        return getattr(module, msg_name)
    except (ValueError, ImportError, AttributeError) as e:
        rospy.logfatal(f"Failed to import message type '{type_str}': {e}")
        rospy.signal_shutdown(f"Invalid message type: {type_str}")
        return None

if __name__ == '__main__':
    rospy.init_node('timescaledb_ingestor_node', anonymous=True)

    # --- Load Parameters ---
    try:
        DB_HOST = rospy.get_param("~db_host")
        DB_PORT = rospy.get_param("~db_port", 5432)
        DB_NAME = rospy.get_param("~db_name")
        DB_USER = rospy.get_param("~db_user")
        DB_PASSWORD = rospy.get_param("~db_password")
        TOPIC_NAME = rospy.get_param("~topic_name")
        TOPIC_MSG_TYPE_STR = rospy.get_param("~topic_msg_type")
        DB_TABLE_NAME = rospy.get_param("~db_table_name")
        COLUMN_MAPPING = rospy.get_param("~column_mapping")
        BATCH_SIZE = rospy.get_param("~batch_size", 100)
        FLUSH_INTERVAL_SECONDS = rospy.get_param("~flush_interval", 5.0)

        if not isinstance(COLUMN_MAPPING, dict) or not COLUMN_MAPPING:
             raise ValueError("'column_mapping' parameter must be a non-empty dictionary.")

    except KeyError as e:
        rospy.logfatal(f"Required parameter missing: {e}. Shutting down.")
        exit(1)
    except ValueError as e:
         rospy.logfatal(f"Parameter error: {e}. Shutting down.")
         exit(1)


    # --- Import Message Type ---
    MsgType = import_message_type(TOPIC_MSG_TYPE_STR)
    if MsgType is None:
         exit(1) # Shutdown initiated in import function

    rospy.loginfo(f"Successfully imported message type: {MsgType.__name__}")

    # --- Connect to DB ---
    connect_db()
    if connection is None:
         rospy.logfatal("Failed to connect to database on startup. Shutting down.")
         exit(1)


    # --- Register Shutdown Hook ---
    rospy.on_shutdown(shutdown_hook)

    # --- Setup Subscriber and Timer ---
    rospy.Subscriber(TOPIC_NAME, MsgType, message_callback, queue_size=BATCH_SIZE*2) # Queue size allows some buffer
    rospy.Timer(rospy.Duration(FLUSH_INTERVAL_SECONDS), timer_callback)

    rospy.loginfo(f"TimescaleDB Ingestor node started for topic '{TOPIC_NAME}'.")
    rospy.loginfo(f"Ingesting to table '{DB_TABLE_NAME}'. Batch size: {BATCH_SIZE}, Flush interval: {FLUSH_INTERVAL_SECONDS}s.")

    rospy.spin() # Keep the node alive until shutdown