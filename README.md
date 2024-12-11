# ETL Data Pipeline


## Description:
ETL Data Pipeline: A Python-based ETL pipeline to extract data from a CSV, transform it (validate emails, format dates, extract domains), and load it into a PostgreSQL database. Includes Docker setup and SQL query scripts for analysis.


## Technologies used:
In this project our team used the following technologies:

- Python
- PostgreSQL
- Docker


## Main features:
- **Data Extraction:**
  Reads data from a CSV file with over 1000 records, including user_id, name, email, and signup_date.
---

- **Data Transformation:**
  - Validates and standardizes signup_date to YYYY-MM-DD.
  - Filters out invalid email addresses.
  - Extracts email domains and adds them as a new column.
---

- **Data Loading:**
  Creates and populates a PostgreSQL table with transformed data.
---

- **SQL Analysis:**
  Provides pre-written SQL scripts for tasks like counting users by signup date and finding the most common email domain.
---


## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Illya-Maznitskiy/etl-data-pipeline.git
    ```
2. Navigate to the project directory:
    ```bash
    cd etl-data-pipeline
    ```
3. Build and run Docker containers:
    ```bash
    docker-compose up --build
    ```
4. Run the ETL process:
    ```bash
    docker exec etl-container python etl.py
    ```
