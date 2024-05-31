class Person:
    def __init__(self, name , age ,Profession):
        self.name = name
        self.age = age
        self.Profession = Profession

    def myfunc(self):
        print("Hello, My name is : " + self.name)
        print( self.age)
        print(self.Profession)

p1 = Person("Ujjwal", 29,"Qa Engineer")
p1.myfunc()





