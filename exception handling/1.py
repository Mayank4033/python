#write a program to findout strike rate of batter using given runs and ball played. 
while(True):

    try:
        run = int(input("enter total runs : "))
        ball = int(input("enter total balls : "))
        strikerate=run/ball
        print("strike rate is : ",strikerate)
        break
    except ZeroDivisionError :
        print("balls cannot be zero")
    except ValueError:
        print("string is not allowed")
