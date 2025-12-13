def calculate(num1,num2):
    add = num1+num2
    sub = num1-num2
    mul = num1*num2
    div = num1/num2
    return add,sub,mul,div

num1=int(input("enter 1st no : "))
num2=int(input("enter 2nd no : "))
result = calculate(num1,num2)
print(result)