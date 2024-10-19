"""Query the database"""

import sqlite3


def query_create():
    conn = sqlite3.connect("women-stem.db")
    cursor = conn.cursor()
    # create execution
    cursor.execute(
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
            VALUES (
                77, 1111, 'DATA SCIENCE', 'Computers & Mathematics', 500 , 300, 200, 0.4, 150000
            )
            """
    )
    conn.commit()
    conn.close()
    return "Create Success"


def query_read():
    conn = sqlite3.connect("women-stem.db")
    cursor = conn.cursor()
    # read execution
    cursor.execute("SELECT * FROM women_stem")
    conn.close()
    return "Read Success"


def query_update():
    conn = sqlite3.connect("women-stem.db")
    cursor = conn.cursor()
    # update execution
    cursor.execute("UPDATE women_stem SET Major = 'NUTRITION SCIENCE' WHERE id = 67 ")
    conn.commit()
    conn.close()
    return "Update Success"


def query_delete():
    conn = sqlite3.connect("women-stem.db")
    cursor = conn.cursor()
    # delete execution
    cursor.execute("DELETE FROM women_stem WHERE id = 76")
    conn.commit()
    conn.close()
    return "Delete Success"
