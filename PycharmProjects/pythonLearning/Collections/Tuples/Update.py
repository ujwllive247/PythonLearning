FruitsName = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# In the case of Tuples.... We are not able to change the items..
#But Python gives a way. .You can change the tuple into the list......and change the items.


#
# x = list(FruitsName)     #changing the tuple into list...
# x[2] = "Ujjwal"
# With append method, we can add the items at the end.
# x.append("Abhay")


# x = ("Abhishek",)  # Add the item at the end of the list....
# FruitsName += x

del FruitsName         # This will throw the error , because the tuple is deleted after the execution of code.....

print(FruitsName)