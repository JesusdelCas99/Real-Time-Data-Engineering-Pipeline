from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, IntegerType
from pyspark.sql.functions import from_json, col, expr
import time


print("KIMI")

# Create a SparkSession builder object for overall configuration and connectors setup for the Kafka cluster
try:
    spark = SparkSession.builder \
    .appName("KafkaCassandraIntegration") \
    .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")
    print("Spark connection created successfully!")

except Exception as e:
    print(f"Couldn't create the spark session due to exception {e}")
                      

# Define the schema for JSON data
schema = StructType().add("id", IntegerType()) \
                     .add("username", StringType()) \
                     .add("password", StringType()) \
                     .add("name", StringType()) \
                     .add("phone", StringType()) \
                     .add("email", StringType()) \
                     .add("city", StringType()) \
                     .add("state", StringType()) \
                     .add("country", StringType())


# Continuously try to create Kafka DataFrame from Kafka topic "userInfoTopic", until successful
while True:
    try:
        # Attempt to create Kafka DataFrame
        df = spark.readStream \
            .format("kafka") \
            .option('kafka.bootstrap.servers', '172.20.10.3:9092') \
            .option("subscribe", "userInfoTopic") \
            .option('startingOffsets', 'earliest') \
            .load()

        # Log success message if Kafka DataFrame is created successfully
        print("Kafka dataframe created successfully")
        break  # Exit loop if Kafka DataFrame is created successfully

    except Exception as e:
        # Log warning message if Kafka DataFrame creation fails
        print(f"Kafka dataframe could not be created because: {e}")
        # Sleep for 5 seconds before next attempt
        time.sleep(5)
        continue  # Continue to retry if Kafka DataFrame creation fails

while True:
    try:
        # Parse message payload to JSON dataframe
        parsed_df = df.selectExpr("CAST(value AS STRING)") \
                    .select(from_json(col("value"), schema).alias("data")) \
                    .select("data.*")


        # Add an artificial "id" column to the dataframe
        parsed_df = parsed_df.withColumn("id", expr("uuid()"))

        # Write parsed data to Cassandra
        query = parsed_df.writeStream \
                        .format("org.apache.spark.sql.cassandra") \
                        .option("keyspace", "spark_stream") \
                        .option("table", "userinfo") \
                        .option("checkpointLocation", "file:///tmp/spark_checkpoint") \
                        .start()

        # Wait for the streaming query to finish before shutting down the SparkSession. This function waits 
        # indefinitely until the streaming query is either stopped manually or encounters an error.
        query.awaitTermination()

        break # Exit loop once kafka application is finished

    except Exception:
        # Log warning message if Kafka DataFrame coud not be broadcasted
        print(f"Kafka dataframe could not be broadcasted to Cassandra. Trying another time...")
        # Sleep for 5 seconds before next attempt
        time.sleep(5)
        continue  # Continue to retry if Kafka DataFrame creation fails