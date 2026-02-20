# <----- INHERITANCE -----> #

# Heirarchial inheritance => one parent class and multiple child classes

class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(A):
    def showC(self):
        print("Class C")

b1 = B()
c1 = C()

b1.showA()
b1.showB()

c1.showA()
c1.showC()
