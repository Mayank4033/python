import matplotlib.pyplot as plt 

Years=[2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]

Matches=[133, 121, 147, 152, 136, 108, 167, 197, 136, 157, 146, 147, 95, 140, 125, 147, 99, 131, 128, 158, 55, 79, 162, 221, 106, 120]
plt.figure(figsize=(10,10))
plt.plot(Years,Matches,color='orange',linewidth=2,marker='o')
plt.title('Odi info')
plt.show()