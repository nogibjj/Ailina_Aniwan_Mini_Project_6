"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query_create, query_read, query_update, query_delete


# Extract
extract()

# Transform and Load
load()

# Query
query_create()
query_read()
query_update()
query_delete()


def results():
    results = {
        "extract": extract(),
        "transform": load(),
        "create": query_create(),
        "read": query_read(),
        "update": query_update(),
        "delete": query_delete(),
    }
    return results
