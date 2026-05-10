import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 

data = pd.read_csv('instagram.csv')
print(data)

plt.figure(figsize=(12,10))
sns.scatterplot(data,x='Age_Group',y='User_Percentage', hue='Age_Group')
plt.xticks(rotation=90)
plt.show()
