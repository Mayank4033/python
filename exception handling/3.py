while True:
    try:
        age=int(input("enter age : "))
        if age<18 or age>60:
            raise ValueError
        else:
            time = 60-age
            print(f"your remaining time for job is :{time} ")
    except ValueError as e:
        if len(e.args)==0:
             print("unusal age for job age must be between 18 to 60 (both including)")
        else:
            print('not a valid age (age must be number)')
    else:
        break
    # finally:
    #     print("thank you")
    