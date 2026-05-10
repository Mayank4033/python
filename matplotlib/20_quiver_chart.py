from matplotlib import pyplot as plt
import numpy as np

x=np.linspace(-3,3,10)
y=np.linspace(-1,1,10)
u=-y
v=x
plt.figure(figsize=(12,4))
plt.quiver(x,y,u,v,color='blue')
plt.grid(True)
plt.show()