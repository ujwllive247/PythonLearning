class A:
   def displayA(self):
      print("Welcome to the team A")


class B(A):
    def displayB(self):
        print("Welcome to the team B")

obj = B()
obj.displayB()
obj.displayA()