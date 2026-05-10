d1 = {'name':'mayank','age':'26','subject':'python','ch':'1,2,3','ch_name':['intro','loop','function']}
d2 = {'name':'abc','age':22,'subject':'django'}

d2.clear()
print(d2)

d2 = d1.copy()
print("copy of d1",d2)

print("d1.get('ch')",d1.get('ch',0))
print("d1.get('add)",d1.get('add','does not exist'))

print(d1.items())

print(d1.keys())
print(d1.values())

print(d1.fromkeys('subject','123'))

print(d2.pop('subject'))
print("d2",d2)

print(d2.popitem())
print(d2)

d2.update({'subject':'python'})
print(d2)