import csv
import re
from datetime import datetime


# Function to validate email
def is_valid_email(email):
    # Simple regex to check valid email format
    email_regex = r"(^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$)"
    return re.match(email_regex, email) is not None


# Function to extract domain from email
def extract_domain(email):
    return email.split("@")[1] if "@" in email else None


# Function to format the signup_date to YYYY-MM-DD
def format_signup_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
    except ValueError:
        return None  # If the date is invalid


# Function to process the data and transform it
def transform_data(input_file, output_file):
    with open(input_file, mode="r", newline="", encoding="utf-8") as infile:
        csv_reader = csv.reader(infile)
        header = next(csv_reader)  # Skip header

        transformed_data = []
        for row in csv_reader:
            user_id, name, email, signup_date = row

            # Validate and transform data
            if is_valid_email(email):
                signup_date = format_signup_date(signup_date)
                domain = extract_domain(email)

                if signup_date:  # Only add valid records
                    transformed_data.append([user_id, name, email, signup_date, domain])

        # Write transformed data to a new file
        with open(output_file, mode="w", newline="", encoding="utf-8") as outfile:
            csv_writer = csv.writer(outfile)
            # Writing header
            outfile.write("user_id,name,email,signup_date,domain\n")
            csv_writer.writerows(transformed_data)


# Call the function with paths to the input and output CSV files
input_file_path = "../data/users.csv"  # Input CSV file path
output_file_path = "../data/transformed_users.csv"  # Output CSV file path
transform_data(input_file_path, output_file_path)
