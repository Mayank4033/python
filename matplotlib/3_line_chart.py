import matplotlib.pyplot as plt 
years=list(range(2000,2025))
print(years)

gdp_growth = [
    7.60, 4.82, 3.80, 7.86, 7.92,
    9.28, 9.26, 7.66, 3.90, 7.86,
    10.26, 6.63, 5.45, 6.39, 7.41,
    8.00, 8.26, 7.17, 6.90, 4.18,
    -7.30, 8.90, 6.99, 9.20, 8.20
]
plt.figure(figsize=(10,10))
plt.plot(years,gdp_growth,linewidth=2,color='blue',marker='o')
plt.title('GDP gowth over 25 years')
plt.show()