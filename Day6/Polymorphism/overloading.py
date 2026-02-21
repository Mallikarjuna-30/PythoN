#<----- POLYMORPHISM ----->#
#<----- OVERLOADING ----->#
# Method Overloading is not possible in python
# same function with different parameters

class calci:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
    
obj = calci()
# print(obj.add(1,2))  # this will give error (Error : missing 1 required positional argument: 'c')
print(obj.add(1,2,3))