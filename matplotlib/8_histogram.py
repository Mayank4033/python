import matplotlib.pyplot as plt 
import numpy as np 
data = np.random.normal(0,10,1000)
print(data)
plt.hist(data,bins=20,density=False,color='orange',label='Data')
plt.legend()
plt.grid(True)
plt.show()