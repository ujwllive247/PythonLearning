class Student:
    def __init__(details,name, age ,parents):
        details.name =name
        details.age = age
        details.parents = parents
        # details.address = address

    # def myfunc(details):
    #     print("My name is " + details.name)


Student1 = Student("Niket", 29 ,"Mr. Shashikant Thakur")

del Student1                 # For del keyword , we can delete the object/ Instance  directly...
print(Student1.parents)