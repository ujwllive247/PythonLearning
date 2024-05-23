FruitsName = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(FruitsName[2])    # This will print the specific item at the mentioned index....
print(FruitsName[2:6])  #This will print the 2nd to 5th Index..........Ignore the 6th element.
print(FruitsName[:5])    # From begining to the 4th item
print(FruitsName[2:])     #From second index item to the end..

#The index -1 refers to the last element, -2 to the second last element, and so on.

if "banana" in FruitsName:    # Check the items present in the list or not.....
    print("Yes, banana is present in the list")
