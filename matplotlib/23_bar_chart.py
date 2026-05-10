from matplotlib import pyplot as plt 
import numpy as np 

years = list(range(2021,2026))
print(years)
web = [80,70,60,50,40]
mobile = [15,25,35,40,30]
ai = [5,5,5,10,30]

plt.bar(years,web,color='blue',label='web')
plt.bar(years,ai,color='yellow',label='ai')
plt.bar(years,mobile,color='green',label='mobile')

plt.legend()
plt.show()