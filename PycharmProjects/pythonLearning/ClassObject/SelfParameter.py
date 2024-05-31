class Student:
    def __init__(details,name, age, parents , address):
        details.name =name
        details.age = age
        details.parents = parents
        details.address = address

    def myfunc(details):
            print("The student name is " + details.name)
            print( "and the age is " + str(details.age))
            print("The Parent's name is " + details.parents)
            print("The student name is " + details.address)

Student1 = Student("Avinash", 15 ,"Mr. Shashikant Thakur" , "Madhubani , Bihar ")

Student1.myfunc()


# class student:
#     def __init__(self, name, age, parents, address):
#         self.name = name
#         self.age = age
#         self.parents = parents
#         self.address = address
#
#         def myfunc(details):
#             print("The student name is " + self.name)
#             print(details.age)
#             print("The student name is " + self.parents)
#             print("The student name is " + self.address)
#
#
# Student1 = student("Avinash", 15, "Mr. Shashikant Thakur", "Madhubani , Bihar ")
#
# Student1.myfunc()
