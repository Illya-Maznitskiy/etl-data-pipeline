import csv
import random
from faker import Faker
from datetime import datetime, timedelta
import os

# Initialize Faker instance
fake = Faker()


# Function to generate random signup date
def generate_signup_date():
    start_date = datetime(2020, 1, 1)
    end_date = datetime.now()
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    signup_date = start_date + timedelta(days=random_days)
    return signup_date


# Create CSV file in 'data/' folder
def generate_csv(num_records=1000):
    # Ensure the 'data' folder exists
    os.makedirs("../data", exist_ok=True)

    csv_file_path = "../data/users.csv"  # Path where CSV will be saved

    with open(csv_file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(["user_id", "name", "email", "signup_date"])

        for user_id in range(1, num_records + 1):
            name = fake.name()
            email = fake.email()
            signup_date = generate_signup_date()

            # Write user data to CSV
            writer.writerow([user_id, name, email, signup_date])

    print(
        f"CSV file with {num_records} records " f"has been created at {csv_file_path}."
    )


# Generate CSV with 1000+ records
generate_csv(1000)
