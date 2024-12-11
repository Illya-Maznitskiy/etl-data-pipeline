import csv
import os
import psycopg2

# Database connection settings from environment
DB_URL = os.getenv("DATABASE_URL", "postgres://myuser:example@db:5432/mydb")


def load_data_to_db(csv_file):
    """Load data from CSV file into the PostgreSQL database."""
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(DB_URL)
        cursor = conn.cursor()

        # Insert data into the database
        with open(csv_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                cursor.execute(
                    """
                    INSERT INTO users (user_id, name, email, signup_date, domain)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (
                        row["user_id"],
                        row["name"],
                        row["email"],
                        row["signup_date"],
                        row["domain"],
                    ),
                )

        conn.commit()
        print("Data successfully loaded into the database.")

    except Exception as e:
        print(f"Error loading data: {e}")
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    # Path to transformed CSV file
    csv_file_path = "../data/transformed_users.csv"

    # Verify CSV file exists
    if not os.path.exists(csv_file_path):
        print(f"File not found: {csv_file_path}")
    else:
        load_data_to_db(csv_file_path)
