import pandas as pd 
sr=pd.Series([100,200,200,400,800,1000],index=['a','b','c','d','e','f'],name='Series')
print(sr)

print(sr.index)
print(sr.values)
print(sr.dtype)
print(sr.name)
print(sr.shape)
print(sr.ndim)
print(sr.size)
print(sr.is_unique)
print(sr.hasnans)