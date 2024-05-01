# when you create a variable inside a function, that variable is local,
# and can only be used inside that function.
# def function():
#     global x
#     x= "Incredible"
#
#
# function()
# print("python is "+ x)


x = "Ujjwal"

def update():
    global x
    x="Abhiranjan"

update()
print(x)  # We can update the value of variable which is written outside the class

