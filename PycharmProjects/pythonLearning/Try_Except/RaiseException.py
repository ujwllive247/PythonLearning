

# x = -1
#
# if x < 0:
#     raise Exception("No, number found which is smaller")






#Question -  Raise a TypeError if x is not an integer

x = "Hello"
if not type(x) is int:
     raise TypeError("Only integers are allowed....")   # Output -   TypeError: Only integers are allowed....
