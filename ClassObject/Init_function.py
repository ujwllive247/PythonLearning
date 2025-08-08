class person:
    def __init__(self,name , age):
        self.name = name
        self.age = age

p1 = person("Ujjwal" , 29)
print(p1.name)
print(p1.age)

# Ujjwal    ........Output of Init function......
# 29

# The __init__() function is called automatically every time the class is being used to create a new object.



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
        # return f"{self.name} ({self.age})"       #Alice (30)

# Create an instance of Person
p = Person("Alice", 30)

# Print the instance
print(p)  # Output: Person(name=Alice, age=30)