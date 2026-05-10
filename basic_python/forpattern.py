# *
# **
# ***
# ****
# *****
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end='')
    print()

print()
# 1
# 22
# 333
# 4444
# 55555
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end='')
    print()

print()
# 1
# 12
# 123
# 1234
# 12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()

print()
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end='')
    print() 

for i in range(5,1,-1):
    for j in range(1,i):
        print("*",end='')
    print() 

# 1
# 22
# 333
# 4444
# 55555
# 4444
# 333
# 22
# 1


for i in range(1,6):
    for j in range(1,i+1):
        print(i,end='')
    print() 

for i in range(5,1,-1):
    for j in range(1,i):
        print(i-1,end='')
    print() 