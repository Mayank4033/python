import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd 

data = pd.read_csv('marks_2.csv')
sns.pointplot(data,x='division',y='maths',hue='gender')
plt.title('Point Plot')
plt.show()