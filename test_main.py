"""
Test goes here
"""

from mylib.extract import extract1, extract2
from mylib.transform_load import load
from mylib.query import query
import os


def test_extract():
    """testing extract"""
    extract1()
    extract2()

    assert os.path.exists("data/women-stem.csv")
    assert os.path.exists("data/recent_grads.csv")


def test_load():
    """testing load"""
    result = load()
    assert result == "Dataset loaded to Databricks or already exists!"


def test_query():
    """testing query"""
    result = query()
    assert result == "Query successful"


if __name__ == "__main__":
    test_extract()
    test_load()
    test_query()

    print("Everything passed!")
