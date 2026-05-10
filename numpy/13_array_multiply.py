import numpy as np 
a=np.array([[10,20,30],[40,50,60],[70,80,90]])
b=np.array([[1,2,3],[4,5,6],[7,8,9]])

# print(a*b)
print(a @ b) #matrix multiplication
print(a.dot(b)) #matrix multiplication


c = np.array([10,20,30,100])
print(c)


print(c.sum())
print(c.mean())
print(c.min())
print(c.max())