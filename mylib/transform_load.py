"""
Transforms and Loads data into the local SQLite3 database

"""

import sqlite3
import csv


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/women-stem.csv"):
    """ "Transforms and Loads data into the local SQLite3 database"""

    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    # skips the header of csv
    next(payload)
    conn = sqlite3.connect("women-stem.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS women_stem")
    c.execute(
        """
        CREATE TABLE women_stem (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            Rank INTEGER, 
            Major_code INTEGER, 
            Major TEXT, 
            Major_category TEXT, 
            Total INTEGER, 
            Men INTEGER, 
            Women INTEGER, 
            ShareWomen FLOAT, 
            Median INTEGER
        )
    """
    )

    valid_rows = [row for row in payload if len(row) == 9]

    # insert
    c.executemany(
        """
        INSERT INTO women_stem (
            Rank, 
            Major_code, 
            Major, 
            Major_category, 
            Total, 
            Men, 
            Women, 
            ShareWomen, 
            Median) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        valid_rows,
    )
    conn.commit()
    conn.close()

    return "women-stem.db"
