import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 

data = pd.read_csv('stream_marks.csv')
sns.stripplot(data,x='Subject',y='Marks')
plt.show()