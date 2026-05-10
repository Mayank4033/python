import numpy as np 
arr1=np.linspace(10,20,num=5)
print(arr1)

arr2,ret=np.linspace(10,100,num=10,retstep=True)
print(arr2,ret)

#create array that has 10 values between 2.0 and 2.5 (start including, also return retvalue 
arr3,step = np.linspace(2.0,2.5,num=10,endpoint=False,retstep=True)
print(arr3,step)