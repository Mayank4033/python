import matplotlib.pyplot as plt
import pandas as pd 
y = [6, 4, 18, 12, 22, 15, 9, 14, 11, 21, 8, 13, 24, 16, 11, 5]
s1=pd.Series(y)
score=s1.cumsum()
x=list(range(1,17))
plt.figure(figsize=(15,8))
plt.plot(x,score)
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.title('Match Score' )
# print(s1)
plt.show()
# plt.legend()