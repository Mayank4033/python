import matplotlib.pyplot as plt

silver_price_change = [-0.42, 1.26, 1.04, -1.03, 2.88, 2.01, 3.93, -4.16, -1.18, 4.38, 0.0, 3.81, 2.76, -0.71, 1.54, 2.83, 1.37, 4.1, 5.02, 2.99, -5.77, 5.71, 6.69, -1.41, 6.9, 6.45, 2.43, 2.37, 7.14, -12.94, -1.49]
dates=list(range(1,32))
# print(dates)
plt.figure(figsize=(12,6))
plt.fill_between(dates,silver_price_change,alpha=0.5)
plt.xlabel('dates')
plt.ylabel('silver_price_change')
plt.title('Silver Price Change')
plt.xticks(dates,rotation=90)
plt.show()