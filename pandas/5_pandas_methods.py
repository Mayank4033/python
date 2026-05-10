import pandas as pd 
sr=pd.Series([10,20,30,404,504],index=['a','b','c','d','e'])
print(sr)

print(sr.head(2))
print(sr.tail(1))
print(sr.to_list())
print(sr.to_dict())
print(type(sr))
name="mayank"
print(type(name))
print(sr.describe())
sr=sr.astype(float)
print(sr)