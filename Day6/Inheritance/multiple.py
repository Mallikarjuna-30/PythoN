# <----- MULTIPLE INHERITANCE -----> #
# Two Parent class and one child class

class A:
    name = "A"
    def showA(self):
        print("Class A")
        
class B:
    name = "B"
    def showB(self):
        print("Class B")
        
class C(B,A):
    def showC(self):
        print("Class C")
        
c1 = C()
print(c1.name)  # B 
c1.showA()
c1.showB()
c1.showC()
