#Collections(Arrays)
#List, Tuple, set, Dictionary

#LIST [] - Ordered and changeable. Allows duplicate members

'''
numList = [1,2,3,4,5,5]
print(type(numList))
numList.append(10)
numList.append(True)
numList.append('test')
print(numList)
print(numList[0])
numList.insert(0,111)
print(numList)
numList.pop(1)
print(numList)
numList2 = ['HI','HELLO']
numList.extend(numList2)
print(numList)

'''

#Tuple() - Ordered & unchangeable. Allows duplicate members
#can do casting
'''
a = (1,2,3,4)
print(a[0])
b = list(a)
print(b)
b.pop()
c = tuple(b)
print(c)
'''

#Set {} - Unordered & unchangeable & unindexed.
# No Duplicate members. duplicates will be removed
# any type of data can be stored
# We cant modify the set item but we can add/remove items
# add(), update(), remove(), pop()
'''
a = {1,2,4,5,4}
print(a)
# a[0] = 10 // not possible
a.add(10)
print(a)
a.remove(4)
print(a)
a.pop()
print(a)
a.update({11,12})
print(a)
'''
#Dictionary{} - ordered & changeable. No Duplicate members
# ANy type of data can be stored
#key:value pair
# get() keys() values() items() update({'DOB': '1/2/3'}),
# thisdict['age'] = '22' thisdict.pop('dept'),del a['age'], a.clear()
'''
a = {
    'name': 'Govi',
    'age': 30,
    'dept': 'IT',
    'location': 'Chennai'
    }
print(a['age'])
print(a.values())
a["age"]=20
a["phone"]=12345678
print(a)

'''



