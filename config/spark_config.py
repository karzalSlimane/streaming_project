from pyspark.sql import SparkSession

# Initialize the Spark session
spark = SparkSession.builder \
    .appName("Kafka PySpark Streaming") \
    .getOrCreate()

# Set the log level to reduce verbosity
spark.sparkContext.setLogLevel("WARN")
