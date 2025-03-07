from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, String, Integer
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Kafka Streaming") \
    .getOrCreate()

# Define schema of incoming data
schema = StructType([
    StructField("user_id", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("location", StringType(), True)
])

# Consume data from Kafka
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9093") \
    .option("subscribe", "user-data") \
    .load()

# Decode the Kafka message
decoded_df = kafka_df.selectExpr("CAST(value AS STRING) AS message")

# Parse the JSON data
json_df = decoded_df.select(F.from_json(F.col("message"), schema).alias("data"))
user_df = json_df.select("data.user_id", "data.age", "data.location")

# Perform transformations (e.g., group by location)
aggregated_df = user_df.groupBy("location").agg(F.avg("age").alias("avg_age"))

# Write the result to the console (for testing)
query = aggregated_df.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
