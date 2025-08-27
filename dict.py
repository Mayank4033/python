d1 = {
    'name':'mayank',
    'age':'26',
    'subject':'python' }

print(d1)
d1['add']='py'
print(d1)

d1['ch']=('1,2,3')
d1['ch_name']=['intro','loop','function']
print("d1",d1)

d2={}
d2['name']='abc'
d2['age']=22
print("d2",d2)

del d1['add']
print(d1)

del d2
print(d2)