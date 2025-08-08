class Student:
    def __init__(details,name, age):
        details.name =name
        details.age = age
        # details.parents = parents
        # details.address = address

    # def myfunc(details):
    #     print("My name is " + details.name)


Student1 = Student("Niket", 29)

Student1.name = "Himanshu"
print(Student1.name)



# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name)
#
# p1 = Person("John", 36)
#
# p1.age = 40
#
# print(p1.age)