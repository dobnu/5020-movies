#HERE is my descent into insanity
import sqlite3
import pandas as pd
con = sqlite3.connect('data/chinook.db')
cur = con.cursor()
df=pd.read_sql_query("SELECT Name FROM Track ORDER BY TrackId LIMIT 5",con)
#sql="SELECT Name FROM Track over /(Partition BY GenreId ORDER BY TrackId DESC)"
#df=pd.read_sql_query("SELECT Name FROM Track RANK() OVER(Partition BY GenreId ORDER BY TrackId DESC)RANK",con)
#print(df)
#df=pd.read_sql_query("SELECT TrackId ,COUNT(*) AS `num` FROM Invoiceline GROUP BY TrackId",con)
#,COUNT(*) AS `num` FROM Invoiceline GROUP BY TrackId
#print(max(df.num))
#This produces a max of 1 and 2 invoices per country so it is negligible to find the best songs
con.close()