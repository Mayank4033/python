def getmin(hour,minutes):
    total_min= hour*60
    total_min+=minutes
    return total_min

hours = int(input("enter hours : "))
minutes = int(input("enter minutes : "))

time=getmin(hours,minutes)
print(f"total minutes : {time}")