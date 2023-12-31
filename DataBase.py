# This code is importing the `sqlite3` module and assigning it the alias `sql`.
import sqlite3 as sql
conn = sql.connect("Name.db")
cur = conn.cursor()
# The `query` variable is storing a SQL query that creates a table named `Player_Name` in the SQLite
# database. The table has two columns, `Player_1` and `Player_2`, both of which are of type `TEXT`.
query = """CREATE TABLE Player_Name(
    Player_1 TEXT,
    Player_2 TEXT
);"""
cur.execute(query)