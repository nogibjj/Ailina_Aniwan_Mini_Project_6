"""
Extract datasets from URLs
"""

import requests
import os


def extract(
    url="https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/college-majors/women-stem.csv",
    url2="https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/college-majors/recent-grads.csv",
    file_path="data/women-stem.csv",
    file_path2="data/recent-grads.csv",
):
    """Extract datasets from URLs and save them to file paths"""

    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Extract the first file
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)

    # Extract the second file
    with requests.get(url2) as r2:
        with open(file_path2, "wb") as f2:
            f2.write(r2.content)

    return file_path, file_path2


if __name__ == "__main__":
    extract()
