import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 

data = pd.read_csv('t20.csv')

sns.lineplot(data=data,x='Year',y='Wins')
plt.show()