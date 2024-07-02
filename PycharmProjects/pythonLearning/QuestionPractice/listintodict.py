list1 = ['a','b','c']
list2 = [1,2,3]

dict1 = dict(zip(list1,list2))
print(dict1)


dict2 = {list1[i]:list2[i] for i in range(len(list1))}

print(dict2)


dict3 = {}

for key in list1:
    for value in list2:
        dict3[key]= value
        list2.remove(value)
        break

print(dict3)        