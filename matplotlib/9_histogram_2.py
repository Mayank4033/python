import matplotlib.pyplot as plt 
import numpy as np 
data=[25,34,45,50,76,89,54,57,40,60,65,68,69]
marks2=[45,76,89,95,56,68,70,50,40,33,30,25]

# y=list(range(1,50,2))
marks=np.array(data)
plt.hist(marks,bins=10,label='Marks of class a',density=False)
plt.hist(marks2,bins=10,label='Marks of class b ',density=False)
plt.xlabel('marks')
plt.ylabel('No of student')
plt.legend()
plt.grid(True)
plt.show()