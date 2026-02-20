# <----- INHERITANCE -----> #

# Multi level inheritance => one parent class and one child class and further the child can have next child class

class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(B):
    def showC(self):
        print("Class C")

c1 = C()
c1.showA()
c1.showB()
c1.showC()