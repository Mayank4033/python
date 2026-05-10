import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 

data = pd.read_csv('heart_attack.csv')
sns.kdeplot(data,x='Age',fill=True)
print(data.columns.tolist())
plt.title('KDE example')
plt.show()