class Student:

    __name="Ravi"       # Private can be created by writing "__" before  variable name

    def __init__(self):
        print(self.__name)
        self.__displayinfo()



    def __displayinfo(self):
        print("Welcome to the coding world")



obj= Student()

# obj.__displayinfo()
