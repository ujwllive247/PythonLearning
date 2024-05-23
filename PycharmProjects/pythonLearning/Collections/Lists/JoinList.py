List1 = ["punjabi", "Haryanavi", "Rajasthani"]
List2 = [20,30,40,50]
List3 = List1 + List2
# print(List3)

#Another way to join two lists is by appending all the items from list2 into list1,   "one by one:"

List1 = ["punjabi", "Haryanavi", "Rajasthani"]
List2 = [20,30,40,50]
# for x in List2:
#     List1.append(x)
#     print(List1)
# output
#     ['punjabi', 'Haryanavi', 'Rajasthani', 20]
#     ['punjabi', 'Haryanavi', 'Rajasthani', 20, 30]
#     ['punjabi', 'Haryanavi', 'Rajasthani', 20, 30, 40]
#     ['punjabi', 'Haryanavi', 'Rajasthani', 20, 30, 40, 50]



# Extend Method.......         it extend the 
List1.extend(List2)
print(List1)


