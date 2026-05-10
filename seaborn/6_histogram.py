import seaborn as sns 
import matplotlib.pyplot as plt 

titanic = sns.load_dataset("titanic")

sns.histplot(titanic,x='age',bins=30,color='skyblue',kde=True)
plt.show()