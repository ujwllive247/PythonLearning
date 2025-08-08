def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c=7, d = 8)


# def my_function(a, b, /, *, c, d):
#   print(a + b + c + d)
#
# my_function(5, 6, 7, d = 8)            #This function throws error.....keyword argument c________ Value...