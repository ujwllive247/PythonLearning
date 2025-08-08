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
