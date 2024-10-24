"""
ETL-Query script
"""

from mylib.extract import extract1, extract2
from mylib.transform_load import load
from mylib.query import query

# Extract
print("Extracting data...")
extract1()
extract2()


# Transform and load
print("Transforming data...")
load()

# Query
print("Querying data...")
query()
