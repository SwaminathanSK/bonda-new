
TIME_SCALE_DB_CONTEXT = """
--- TIMESCALEDB CONTEXT, CONCEPTS, AND EXAMPLES ---

This database uses TimescaleDB, an extension of PostgreSQL engineered for time-series data. In TimescaleDB, data is stored in hypertables – a logical abstraction that partitions data based on time (and optionally by other dimensions), allowing for high-performance inserts, queries, and automated maintenance.

Below are key concepts, guidelines, and diverse examples that illustrate how to work with TimescaleDB.

1. Hypertables:
   - A hypertable is created from a normal PostgreSQL table to optimize it for time-series workloads.
   - It partitions data into smaller “chunks” automatically, based on a specified time column.
   
   Example:
   --------------------------------------------
   CREATE TABLE sensor_data (
       time        TIMESTAMPTZ NOT NULL,
       sensor_id   INT,
       temperature DOUBLE PRECISION,
       humidity    DOUBLE PRECISION
   );
   
   SELECT create_hypertable('sensor_data', 'time');
   --------------------------------------------
   This command transforms sensor_data into a hypertable, partitioning it by the time column.

2. Time Bucketing:
   - Use time_bucket() to group data into fixed intervals for aggregation.
   
   Example 1: Group CPU usage data into hourly buckets:
   --------------------------------------------
   SELECT time_bucket('1 hour', ts) AS bucket,
          AVG(cpu_usage) AS avg_cpu
   FROM metrics
   WHERE ts > NOW() - INTERVAL '1 day'
   GROUP BY bucket
   ORDER BY bucket;
   --------------------------------------------
   
   Example 2: For sensor readings, group by 15-minute intervals:
   --------------------------------------------
   SELECT time_bucket('15 minutes', time) AS interval,
          MAX(temperature) AS max_temp,
          MIN(temperature) AS min_temp
   FROM sensor_data
   WHERE time > NOW() - INTERVAL '6 hours'
   GROUP BY interval
   ORDER BY interval;
   --------------------------------------------

3. Gap Filling:
   - Use time_bucket_gapfill() when your data may have missing intervals to generate continuous time series.
   
   Example: Fill in missing data and carry forward the last observation:
   --------------------------------------------
   SELECT time_bucket_gapfill('5 minutes', time) AS interval,
          locf(AVG(temperature)) AS avg_temp
   FROM sensor_data
   WHERE time > NOW() - INTERVAL '1 day'
   GROUP BY interval
   ORDER BY interval;
   --------------------------------------------
   Note: locf() stands for “last observation carried forward” and can be replaced with interpolate() if required.

4. Filtering on Recent Data:
   - Always filter time-series queries using NOW() - INTERVAL to limit the dataset.
   
   Example:
   --------------------------------------------
   SELECT *
   FROM sensor_data
   WHERE time > NOW() - INTERVAL '7 days';
   --------------------------------------------

5. Continuous Aggregates:
   - Continuous aggregates are materialized views that automatically update as new data arrives, providing efficient aggregated results.
   
   Example: Create a continuous aggregate for daily average temperature:
   --------------------------------------------
   CREATE MATERIALIZED VIEW daily_avg_temperature WITH (timescaledb.continuous) AS
   SELECT time_bucket('1 day', time) AS day,
          AVG(temperature) AS avg_temp
   FROM sensor_data
   GROUP BY day;
   --------------------------------------------
   Query the continuous aggregate just like a regular table:
   --------------------------------------------
   SELECT * FROM daily_avg_temperature ORDER BY day;
   --------------------------------------------

6. Approximate Aggregations (TimescaleDB Toolkit):
   - TimescaleDB Toolkit provides advanced data types and functions for approximate aggregations over large data sets.
   
   Example: Use tdigest for calculating approximate percentiles:
   --------------------------------------------
   SELECT approx_percentile(0.95, temperature) AS p95_temperature
   FROM sensor_data
   WHERE time > NOW() - INTERVAL '30 days';
   --------------------------------------------
   
   Example: Use HyperLogLog (if available) for an approximate distinct count:
   --------------------------------------------
   SELECT hll_cardinality(hll_add_agg(sensor_id)) AS distinct_sensors
   FROM sensor_data;
   --------------------------------------------
   Note: These functions are available via the TimescaleDB Toolkit extension.

7. Best Practices and Guidelines:
   - When working with hypertables, always reference the designated time column (e.g., time, ts).
   - Use time_bucket() for grouping rather than relying on standard PostgreSQL functions like DATE_TRUNC() for better performance.
   - Apply time_bucket_gapfill() in queries where missing intervals are expected.
   - Filter the dataset with time-based conditions (e.g., NOW() - INTERVAL 'X') to optimize performance.
   - When available, leverage continuous aggregates for recurring queries over large time ranges.
   - Use approximate functions like approx_percentile() or HyperLogLog in scenarios where exact results are less critical than performance.

--- END OF TIMESCALEDB CONTEXT ---
"""