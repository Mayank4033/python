import matplotlib.pyplot as plt 
import numpy as np

x= np.linspace(1,10,10)
y=np.sin(x)
error=0.8 #bar height
plt.errorbar(x,y,yerr=error,label='error chart')
plt.legend()
plt.title('Error Bar Chart')
plt.grid('true')
plt.show()