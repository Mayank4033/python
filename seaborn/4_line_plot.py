import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 

data = sns.load_dataset("titanic")

tit=data.dropna(subset=['age','survived'])

sns.lineplot(data=tit,x='age',y='survived')
plt.xlabel('Age')
plt.ylabel('Survived')
plt.title('Line Plot')
plt.show()