

# Hiding the implementation details of class and only showing the essential feature to the user.

# Encapsulation >>>> Wrapping data and function into a single unit....


class Car:
    def __init__(self):
        self.accelerator= False
        self.brk = False
        self.clutch = False


    def start(self):
        self.clutch=True
        self.accelerator = True
        print("car started....")

car1 = Car()
car1.start()