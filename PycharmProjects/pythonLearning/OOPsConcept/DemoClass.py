class DemoClass:
    a = 10
    def sumValue(self):
        print(20+30)

demoobject = DemoClass()
demoobject1 = DemoClass()

demoobject.sumValue()   # calling the function , from object....

print(demoobject.a)   # Calling Variable from other object....
print(demoobject1.a)