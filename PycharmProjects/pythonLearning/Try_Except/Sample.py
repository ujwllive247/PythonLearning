# The try block lets you test a block of code for errors.
#
# The except block lets you handle the error.
#
# The else block lets you execute code when there is no error.
#
# The finally block lets you execute code, regardless of the result of the try- and except blocks.


x =5

try:
    print(x)
except:
    print("An exception occurred")   # When x is not defined....
else:
    print("Code executed")  #Code executed , when x is defined....