import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(10,100,10)
y = np.random.rand(1,100,10)

plt.hexbin(x,y,cmap='summer_r',gridsize=40)
plt.colorbar(label='Counts')
plt.show()