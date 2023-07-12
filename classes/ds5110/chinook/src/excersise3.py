import sqlite3
import pandas as pd
con = sqlite3.connect('data/chinook.db')
cur = con.cursor()
# Get all the table names
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
df = pd.read_sql_query("SELECT Name FROM Track WHERE Name like '%rock%' ORDER BY Composer", con)
print(df)
df=pd.read_sql_query("SELECT COUNT( DISTINCT Composer) FROM Track WHERE Composer like '%Jimmy%' ",con)
print(df)
con.close()