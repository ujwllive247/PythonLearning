class Student:

    __name="Ravi"       # Private can be created by writing "__" before  variable name

    def __init__(self):
        print(self.__name)


obj= Student()
