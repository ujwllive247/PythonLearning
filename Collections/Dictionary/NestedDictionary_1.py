Person1 ={
    "name" : "Himanshu",
    "age" : 25
}

Person2 ={
    "name" : "Alok",
    "age" : 27
}
Person3 ={
    "name" : "Abhishek",
    "age" : 30
}

friends = {                              # We can assign the dictionary to the other dictionary after creating...
    "Person1" : Person1,
    "Person2": Person2,
    "Person3": Person3
}
# print(friends)

# Access the items from dictionary......

# print(friends["Person2"]["name"])      #Access the items from dictionary......


# Loops through nested dictionary....
for x, obj in friends.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])


