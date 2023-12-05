import csv
from faker import Faker
from multiprocessing import Pool, cpu_count

# Initialize Faker with French locale
fake = Faker('fr_FR')


def generate_data():
    """ Generate a single row of French data """
    first_name = fake.first_name()
    last_name = fake.last_name()
    address = fake.address().replace("\n", ", ")
    post_code = fake.postcode()
    city = fake.city()
    return [first_name, last_name, address, post_code, city]

def write_chunk(chunk_size, file_name):
    """ Write a chunk of data to the file """
    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for _ in range(chunk_size):
            writer.writerow(generate_data())

def create_large_csv(target_size_gb, file_name):
    chunk_size = 10000  # Adjust as needed for optimal performance
    num_chunks = (target_size_gb * (10**9)) // (sum([len(str(element)) for element in generate_data()]) * chunk_size)

    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["First Name", "Last Name", "Address", "Post Code", "City"])

    with Pool(cpu_count()) as pool:
        for _ in range(num_chunks):
            pool.apply_async(write_chunk, args=(chunk_size, file_name))

        pool.close()
        pool.join()

# Run
if __name__ == '__main__':
    file_name = "large_file.csv"
    target_size_gb = 10  # Target file size in GB
    create_large_csv(target_size_gb, file_name)
