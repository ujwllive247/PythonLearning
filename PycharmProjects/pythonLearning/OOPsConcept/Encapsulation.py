


class Student:
    def __init__(self):
        self.__name=""

    def getname(self):
        return self.__name

    def setname(self,name):
        self.__name=name


obj = Student()
obj.setname("Check name printed or not")

name=obj.getname()

print(name)


