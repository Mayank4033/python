import pandas as pd 
import connection as con
sql="select * from payment"
sr=pd.read_sql(sql,con.database)
print(sr)

sr2=pd.read_json('marks1.json').squeeze()
print(sr2)

