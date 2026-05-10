import numpy as np 
arr1=np.array([1,2,3,4,5])
arr2 =np.array([[10,20,30],[40,50,60]])
print(arr1)
print(arr2)

print(arr1[0])
print(arr1[0:4])

print(arr2[0,2])
print(arr2[1,0])

print(arr2[0:2,0:2])
print(arr2[arr2>20])