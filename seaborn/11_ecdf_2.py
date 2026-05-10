import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 

data=pd.read_csv('car_sales.csv')

car_sales=data.melt(
    id_vars='Week',
    value_vars=['Swift','WagonR','Baleno'],
    value_name='Sales',
    var_name='Model')

plt.figure(figsize=(12,10))
sns.ecdfplot(data=car_sales,x='Sales',hue='Model')
plt.show()