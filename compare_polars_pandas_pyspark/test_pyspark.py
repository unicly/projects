from pyspark.sql import SparkSession
import time

# Initialize a Spark session
spark = SparkSession.builder.appName("csvRead").getOrCreate()

# Path to your CSV file
csv_file_path = 'large_file.csv'

# Start the timer
start_time = time.time()

# Load the CSV file with PySpark
df = spark.read.csv(csv_file_path, header=True, inferSchema=True)

# Delete the 'city' column
df = df.drop('City')

# End the timer
end_time = time.time()

# Display the first 5 lines
df.show(5)

# Print the execution time
print("Execution Time: {:.2f} seconds".format(end_time - start_time))

# Stop the Spark session
spark.stop()
