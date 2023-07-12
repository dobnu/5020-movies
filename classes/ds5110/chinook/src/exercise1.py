import sqlite3
import pandas as pd
con = sqlite3.connect('data/chinook.db')
cur = con.cursor()

# Get all the table names
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
df=pd.read_sql_query("SELECT InvoiceId, MAX(Total) FROM Invoice", con)
print(df)
df = pd.read_sql_query("SELECT TrackId,UnitPrice FROM InvoiceLine WHERE InvoiceID= '404'", con)
print(df)
mylist=tuple(df.TrackId)
df = pd.read_sql_query(f'SELECT Name FROM Track WHERE TrackId in {format(mylist)}',con)
print(df)
con.close()