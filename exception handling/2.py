numbers=[10,13,30,'mayank','hii',10.25]
sum=0
avg=0
count=0
for num in numbers:
    try:
        sum=sum+num
        count=count+1
    except TypeError:
        print(f"{num} is an invalid type,hence skipped ")
print("sum of all elements is : ",sum)
print("total number of valid elements : ",count)

try:
    avg=sum/count
    print("average is : ",avg)
except ZeroDivisionError:
    print("no valid elements in the list")
    