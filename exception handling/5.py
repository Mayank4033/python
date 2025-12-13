from datetime import datetime as dt

while True:
    try:
        date=input("enter the appointment date (dd-mm-yyyy) : ")
        apt=dt.strptime(date,"%d-%m-%Y")
        if apt<dt.today():
           raise ValueError("your appointment date should be future date only")
    except ValueError as e :
            if e.args[0].find('appointment')<0:
                print("invalid date")
            else:
                print(e)
    else:
        print(f"Appointment booked successfully on {apt}") 
        break
    finally:
        print("thank you!")