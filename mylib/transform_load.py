"""
Transforms and Loads data into the databricks database
"""

import os
from databricks import sql
import csv
from dotenv import load_dotenv


# Load the csv files and insert into a new Databricks database
def load(dataset="data/women-stem.csv", dataset2="data/recent-grads.csv"):
    """Transforms and Loads data into the Databricks database"""
    load_dotenv()

    with open(dataset, newline="") as file1, open(dataset2, newline="") as file2:
        payload = csv.reader(file1, delimiter=",")
        payload2 = csv.reader(file2, delimiter=",")
        # Skip the header of CSV
        next(payload)
        next(payload2)

        with sql.connect(
            server_hostname=os.getenv("server_hostname"),
            http_path=os.getenv("http_path"),
            access_token=os.getenv("access_token"),
        ) as connection:
            with connection.cursor() as cursor:
                # Create women_stem table
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS women_stem (
                    rank INT, 
                    major_code INT, 
                    major STRING, 
                    major_category STRING, 
                    total INT, 
                    men INT, 
                    women INT, 
                    sharewomen FLOAT, 
                    median INT);"""
                )

                # Check if the table is empty and insert data if needed
                cursor.execute("SELECT * FROM women_stem")
                result = cursor.fetchall()
                if not result:
                    insert_query = (
                        """INSERT INTO women_stem VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
                    )
                    cursor.executemany(insert_query, payload)

                # Create recent_grads table
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS recent_grads (
                    rank INT,
                    major_code INT,
                    major STRING,
                    total INT,
                    men INT,
                    women INT,
                    major_category STRING,
                    sharewomen FLOAT,
                    employed INT,
                    full_time INT,
                    part_time INT,
                    unemployed INT,
                    unemployment_rate FLOAT,
                    median INT);"""
                )

                # Check if the recent_grads table is empty and insert data if needed
                cursor.execute("SELECT * FROM recent_grads")
                result = cursor.fetchall()
                if not result:
                    insert_query_2 = """INSERT INTO recent_grads VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
                    cursor.executemany(insert_query_2, payload2)

    return "Dataset loaded to Databricks or already exists!"


if __name__ == "__main__":
    load()
