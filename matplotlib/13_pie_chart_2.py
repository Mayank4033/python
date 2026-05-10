import matplotlib.pyplot as plt 
percentage=[70,65,50,80,75,90,60]
students=['mayank','pari','mohit','moksh','hitu','chirag','ronak']
plt.pie(percentage,labels=students,autopct='%.1f%%')
plt.show()