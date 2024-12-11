import csv
import os


# Define the file path
csv_file_path = os.path.join(os.path.dirname(__file__), "../data/users.csv")

# Open the CSV file
with open(csv_file_path, mode="r", newline="", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    # Skip header if present
    next(csv_reader)
    # Loop through rows
    for row in csv_reader:
        print(row)  # You can process each row as needed
