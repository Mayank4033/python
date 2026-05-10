import matplotlib.pyplot as plt 
data = {
    2008: 0,
    2009: 1,
    2010: 1,
    2011: 4,
    2012: 5,
    2013: 4,
    2014: 4,
    2015: 1,
    2016: 3,
    2017: 6,
    2018: 5,
    2019: 5,
    2020: 0,
    2021: 1,
    2022: 2,
    2023: 3,
    2024: 2,
    2025: 3,
    2026: 1  # As of Jan 28, 2026 – year still ongoing
}
years=list(data.keys())
print(years)
century=list(data.values())
print(century)
plt.bar(years,century)
plt.title('virat kohli century')
plt.xlabel('years')
plt.ylabel('centuries')
plt.xticks(years,rotation=90)
plt.show()