
# Double the input sent...........
def multiplier(n):
    return lambda a : a*2

multiplire = multiplier(2)
print(multiplire(11))



# def myfunc(n):
#   return lambda a : a * n
#
# mydoubler = myfunc(2)
#
# print(mydoubler(11))


# Tripler the input send....

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)        # This line perform actions....

print(mytripler(11))


#use the same function definition to make both functions, in the same program:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))