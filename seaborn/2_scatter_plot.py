import seaborn as sns 
import matplotlib.pyplot as plt 

data = sns.load_dataset('titanic')
sns.scatterplot(data,x='age',y='survived')
plt.show()