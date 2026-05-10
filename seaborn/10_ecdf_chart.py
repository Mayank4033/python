import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 

data = sns.load_dataset("titanic")
data_clean=data.dropna(subset=['age'])
sns.ecdfplot(data=data_clean,x='age',color='blue')
plt.title('ECDF Chart')
plt.show()