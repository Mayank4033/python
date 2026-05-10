import matplotlib.pyplot as plt 
import numpy as np 

x=np.linspace(-2,2,10)
y=np.linspace(-2,2,10)

x,y=np.meshgrid(x,y)
u=-y
v=x
plt.streamplot(x,y,u,v)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()