import polars as pl
import time

# Path to your CSV file
csv_file_path = 'large_file.csv'

# Start the timer
start_time = time.time()

# Load the CSV file with Polars
df = pl.read_csv(csv_file_path)

# Delete the 'city' column
df = df.drop('City')

# End the timer
end_time = time.time()

# Display the first 5 lines
print(df.head())

# Print the execution time
print("Execution Time: {:.2f} seconds".format(end_time - start_time))
