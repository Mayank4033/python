l1 = [123,30.30,'I','am','mayank','santwani']
l2 = ['batch','python',30]

print(l1)

l1.append('hey')
print("append",l1)

l1.extend(l2)
print("extend",l1)

l1.insert(2,'heyy!')
print("insert",l1)

l1.remove('hey')
print("remove",l1)

l1.pop(6)
print("pop",l1)

l2.clear()
print("clear",l2)

print("index",l1.index('mayank'))

print("count",l1.count('python'))

l2=[1,3,6,8,10,13,2]
l2.sort()
print("sort",l2)

l2.reverse()
print("reverse",l2)

l3=l2.copy()
print("l3",l3)

l4=[]
l4.extend(['bca','bba','bcom'])
print("l4",l4)