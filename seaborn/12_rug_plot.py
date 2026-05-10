import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 

data = sns.load_dataset('titanic')
data_clean = data.dropna(subset=['age'])
sns.rugplot(data_clean,x='age',height=0.1,color='blue')
plt.show()