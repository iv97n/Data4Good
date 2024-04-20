from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("ETLExample") \
    .getOrCreate()

print("Hello from pyspark")