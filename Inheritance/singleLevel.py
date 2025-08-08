class A():
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature2 is working")

class B(A):                # B inherit the A functions.........
    def feature3(self):
        print("Feature 3 is working")

    def featire4(self):
        print("Feature 4 is working")

class c(A,B):
    print("Feature 5 is working")


a1 = A()
a1.feature1()
a1.feature2()


b1 = B()

b1.feature1()

c1 =c()
c1.featire4()
