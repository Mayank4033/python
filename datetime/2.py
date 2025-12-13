import datetime

def getdate():
    year=int(input("enter year : "))
    month=int(input("enter month : "))
    day=int(input("enter day : "))

    date=datetime.date(year,month,day)
    print(date)

getdate()

def parsedate():
    date=input("enter date (yyyy-mm-dd) : ")

    parsedate=datetime.date.fromisoformat(date)
    print(parsedate)

parsedate()