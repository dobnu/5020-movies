#HERE is my descent into insanity
import sqlite3
import pandas as pd
con = sqlite3.connect('data/chinook.db')
cur = con.cursor()
def makedict(dbname,mergeobject,bigbdname):
  df_name=pd.read_sql_query("SELECT {1}, {0} FROM {2}".format(dbname,mergeobject,bigbdname),con)
  df_name=df_name.set_index(mergeobject, drop=True)
  mydict=df_name.to_dict()
  mydict=mydict[dbname]
  return mydict
#2.1
df=pd.read_sql_query("SELECT Invoice.BillingCountry, InvoiceLine.TrackId  FROM InvoiceLine INNER JOIN Invoice ON InvoiceLine.InvoiceId=Invoice.InvoiceId", con)
df=df['TrackId'].value_counts()
df=df.reset_index()
df.columns=['Trackid','counters']
print(df.sort_values(by=['counters','Trackid'],ascending=[False,True]).head(5))
#2.2
df=pd.read_sql_query("SELECT Invoice.BillingCountry, InvoiceLine.TrackId, Track.Name  FROM InvoiceLine INNER JOIN Invoice ON InvoiceLine.InvoiceId=Invoice.InvoiceId INNER JOIN Track ON InvoiceLine.TrackId=Track.TrackId", con)
df2 = df.groupby(['BillingCountry'])['TrackId'].value_counts()
df2.groupby(level=[0,1]).nlargest(5)
country=[]
trackid=[]
for i in df2.index:
  country.append(i[0])
  trackid.append(i[1])
values2=df2.tolist()
df = pd.DataFrame(list(zip(country, trackid, values2)),columns =['country', 'trackid','counters'])
print(df.sort_values(by=['country','counters','trackid'],ascending=[True,False,True]))
#2.3
mydict=makedict('Name','TrackId','Track')
df['name']=df['trackid'].apply(lambda x: mydict[x])
print(df[['country', 'name']])
#2.4
mydict=makedict('AlbumId','TrackId','Track')
df['AlbumId']=df['trackid'].apply(lambda x: mydict[x])
mydict=makedict('ArtistId','AlbumId','Album')
df['ArtistId']=df['AlbumId'].apply(lambda x: mydict[x])
mydict=makedict('Name','ArtistId','Artist')
df['Artist_name']=df['ArtistId'].apply(lambda x: mydict[x])
print(df[['country', 'name','Artist_name']])
con.close()