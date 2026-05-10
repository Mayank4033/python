import matplotlib.pyplot as plt 

years=range(2001,2026)
india_debt_gdp_ratio = [
    70.6, 75.8, 77.0, 77.2, 74.4, 70.4, 67.5, 68.3, 64.9, 60.1, 
    62.0, 62.1, 61.8, 62.4, 62.0, 62.2, 63.1, 63.8, 67.4, 88.5, 
    83.7, 83.1, 82.0, 81.5, 80.8
]
print(len(india_debt_gdp_ratio))

plt.figure(figsize=(12,4))
plt.step(years,india_debt_gdp_ratio)
plt.title("Step Chart")
plt.xlabel("Years")
plt.ylabel("Ratio")
plt.show()