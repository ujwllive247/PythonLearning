
#if you send a List as an argument, it will still be a List when it reaches the function:

def my_function(fruits):
    for x in fruits:
        print(x)
fruits = ["Orange","Apple","Banana"]
my_function(fruits)