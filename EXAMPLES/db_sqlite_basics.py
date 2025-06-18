import sqlite3
from pprint import pprint
from db_iterrows import iterrows_asdict

# conn = sqlite3.Connection(...)
with sqlite3.connect("../DATA/presidents.db") as conn:  # connect to the database

    s3_cursor = conn.cursor()  # get a cursor object

    # select specified columns from all presidents
    s3_cursor.execute('''
        select termnum, firstname, lastname, party
        from presidents
    ''')  # execute a SQL statement

    pprint(list(iterrows_asdict(s3_cursor)))
    

