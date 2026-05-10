import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 

data = pd.read_csv('marks.csv')

sns.rugplot(data,x='Exam_Mark',height=0.5,color='orange')
plt.show()