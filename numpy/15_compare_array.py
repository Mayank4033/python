import numpy as np 

arr1=np.array([10,20,30])
arr2=np.array([10,20,30])
arr3=np.array([10,200,300])
arr4=np.array([[10,20,30]])

print(np.array_equal(arr1,arr2))
print(np.array_equal(arr1,arr3))
print(np.array_equal(arr1,arr4))