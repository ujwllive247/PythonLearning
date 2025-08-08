class person:
    def __init__(self,name, age,Address):
        self.name = name
        self.age = age
        self.Address = Address

    def printname(self):
        print(self.name, self.age)


class student(person):
    pass

x = student("Ujjwal",20,"New Delhi, India")

x.printname()
# x.printAddress()
