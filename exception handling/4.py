from datetime import datetime
while True:
    try:
        date=input("enter your dob(dd-mm-yyyy) : ")
        print(date)
        dob=datetime.strptime(date,"%d-%m-%Y")
        print(dob)
        break
    except ValueError:
        print("invalid format enter valid date")

    