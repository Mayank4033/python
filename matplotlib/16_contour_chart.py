import matplotlib.pyplot as plt 
import numpy as np

years=np.array([2018,2019,2020,2021,2022,2023])
teams = ["India", "Australia", "England", "Pakistan", "South Africa"]
team_indices=np.arange(len(teams))
print(team_indices)

x,y=np.meshgrid(years,team_indices)
# print(y)

# Each row represents a team, each column a year
centuries = np.array([
    [12, 15, 8, 10, 14, 18],  # India
    [10, 11, 7, 9, 12, 11],   # Australia
    [8, 14, 10, 11, 15, 13],  # England
    [5, 6, 9, 12, 11, 10],    # Pakistan
    [7, 8, 5, 4, 8, 9]        # South Africa
])


plt.contour(x,y,centuries,levels=4)
plt.yticks(team_indices, teams) # Map numbers back to Team Names

plt.show()