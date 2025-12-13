def sumavg(*numbers):
    sum=0
    for num in numbers:
        sum+=num
        avg=sum/len(numbers)
        return sum,avg

result=sumavg(10,20,30,40)
print(result)

result=sumavg(11,22,33)
print(result)