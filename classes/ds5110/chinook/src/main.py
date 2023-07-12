import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
con = sqlite3.connect('data/chinook.db')
cur = con.cursor()
# Get all the table names
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
df=pd.read_sql_query("SELECT * FROM Track", con)
df['time']=df.Milliseconds.apply(lambda x: x/60000)
df['time']
g=sns.histplot(df['time'],binwidth=1.6)
g.title("Music in Min")
g.xlabel("Time in Min")
g.savefig('img/fig1.png')
con.close()
