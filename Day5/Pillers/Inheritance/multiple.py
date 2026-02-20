# <----- INHERITANCE -----> #

# Multiple inheritance => one parent class and one child class

class A:
    def showA(self):
        print("Class A")

class B:
    def showB(self):
        print("Class B")

class C(A,B):
    def showC(self):
        print("Class C")

c1 = C()
c1.showA()
c1.showB()
c1.showC()