fruits = ("apple", "banana", "cherry","Rashperry","sdfsdf","sdfsdfd","erer3")
# (green, *yellow) = fruits #                  ("apple", "banana", "cherry","Rashperry")
# print(blue)
# print(yellow)           # When we add asterisk at the begining of variable then rest values are assigned to that variable.


#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

# Example -1
(green,*yellow,red) = fruits
print(green)
print(yellow)         # leave last item because of asterisk..
print(red)
