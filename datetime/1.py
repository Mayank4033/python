import datetime

date1=datetime.date(2025,12,15)
date2=datetime.date(2002,12,15)
print(date1>date2)

btime1=datetime.datetime(2011,3,12,10,55,20)
btime2=datetime.datetime(2023,2,15,7,45,5)
print(btime2-btime1)

p1=datetime.timedelta(950,45)
p2=datetime.timedelta(450,15)
gap=p1-p2
print(gap)

today = datetime.date.today()
print(today)

now=datetime.datetime.now()
print(now)

indformat=now.strftime("%a-%d/%m/%y %H-%M-%S")
print(indformat)