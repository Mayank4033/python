import numpy as np 
arr1=np.array([10,20,30])
arr2=np.array([10,20,30])

res_and=np.logical_and(arr1<=15,arr2>5)
print(res_and)

res_or=np.logical_or(arr1<=15,arr2>20)
print(res_or)

logical_not=np.logical_not(arr1>50)
print(logical_not)

logical_xor=np.logical_xor(arr1<15,arr2>25)
print(logical_xor)