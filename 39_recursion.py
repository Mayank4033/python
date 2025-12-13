def getFactorial(number):
    if number == 1 or number == 0:  # base case
        return 1
    else:
        return number * getFactorial(number - 1)  # recursive case

number = int(input("Enter number to get factorial: "))
factorial = getFactorial(number)
print("Factorial =", factorial)
