"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

food dataset
"""

import requests


def extract(
    url="https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/college-majors/women-stem.csv",
    file_path="data/women-stem.csv",
):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
