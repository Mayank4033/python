import matplotlib.pyplot as plt 
import numpy as np 

x=np.arange(1,11)
y=np.arange(1,11)
print(x)

plt.polar(x,y,color='red')
plt.show()