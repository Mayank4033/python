import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd

titanic=sns.load_dataset('titanic')
titanic_age=titanic.dropna(subset=['age'])
sns.kdeplot(titanic_age,x='age',y='survived',fill=True,color='orange')
plt.title('Kde plot of passenger age ')
plt.show()