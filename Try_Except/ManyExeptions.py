


try:
    print(x)
except NameError:
    print("Variable x is not defined.")   # Name Error will be printed when x is not defined.
except:
    print("Someting went wrong")