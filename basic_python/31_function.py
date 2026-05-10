def printline():  #without return value without argument
    print("_"*100)
    return None


def printletter(letter,times): #without return value with argument
    print(letter*times)

def pi(): #with return value without argument
    pi=3.141516
    return pi

def tocelcius(fahrenheit): #with return value with argument
    celsius = (fahrenheit-32)*(5/9)
    return celsius

printletter('~',100)
printline()
pi=pi()
print(f"value of pi is : {pi}")

fahrenheit = int(input("enter fahrenheit : "))
celsius = tocelcius(fahrenheit)
print(f"celsius is : {celsius}")