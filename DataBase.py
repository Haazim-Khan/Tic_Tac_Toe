# This code is importing the `sqlite3` module and assigning it the alias `sql`.
import sqlite3 as sql
try:
    conn = sql.connect("Name.db")
    cur = conn.cursor()
except:
    print("Could not connect to Database")
# The `query` variable is storing a SQL query that creates a table named `Player_Name` in the SQLite
# database. The table has two columns, `Player_1` and `Player_2`, both of which are of type `TEXT`.
query = """CREATE TABLE Player_Name(
    Player_1 TEXT,
    Player_2 TEXT
);"""
def table_exists(table_name):
    # Query the sqlite_master table to check for the existence of the table
    try:
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        result = cur.fetchone()
    except:
        print("Error While Executing")
    if not(result):
        cur.execute(query)
        conn.close()
table_exists("Player_Name")