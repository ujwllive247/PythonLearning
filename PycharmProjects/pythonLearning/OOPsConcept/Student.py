

class Student:
    name = "Ujjwal Kumar"
    # school = "xt javier school"
    # phone = 1345487888
    # address = "Berbingham, London"

    def __init__(self, school, phone):
        self.school = school
        self.phone = phone
        print("Adding new student into database")






s1=Student("xt- javier" , 123456)
print(s1.school,s1.phone)
print(s1.name)
# print(s1.address)