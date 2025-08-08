


# Tuple is ordered or unchangeable in nature, it is written in round bracket.

Hardware = ("Keyboard", "Mouse", "Desktop", "Laptop")
print(Hardware)



# Tuples allow duplicate value
Hardware = ("Keyboard", "Mouse", "Desktop", "Laptop", "Mouse")
print(Hardware)
print(len(Hardware))     # Print length of the tuple  ______Output  -----5.



# Way to create tuple with only one item ,
Name = ("Ujjwal")     # This is not a tuple, it is a string.....
Name = ("Alok",)       # This is tuple
print(type(Name))



# Tuple items should be string , Integer and Boolean......   and also the combination of these.....
Name = ("Ujjwal", "Alok", True, "Himanshu", 20)
print(Name)          # ('Ujjwal', 'Alok', True, 'Himanshu', 20)

# Using the tuple method..... We can create the tuple ..
Name = tuple(("Secninjaz"))          # Earlier this is just a string but now using tuple method this is converted into tuple.....also we call this constructor...
print(type(Name))