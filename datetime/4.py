import datetime as dt 

# print(dt.datetime.now())

# print(dt.datetime.today())

# indformat=dt.datetime.now().strftime("%d-%m-%y")
# print(indformat)

p1=input("enter date of person1 : ")
date=dt.datetime.strptime(p1,"%d-%m-%y")
print(date)

p2=input("enter date of person2 : ")
date2=dt.datetime.strptime(p2,"%d-%m-%y")
print(date)

if date<date2:
    print("person1 is elder")
else:
    print("person2 is elder")