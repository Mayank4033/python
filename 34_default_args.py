def toinch(meter,foot=0,inches=0):
    temp=(foot*12)+inches
    temp1=(meter*3.281*12)
    result = temp+temp1
    return result

result=toinch(2,5,3)
print(result)

result=toinch(2,4)
print(result)

result=toinch(2)
print(result)