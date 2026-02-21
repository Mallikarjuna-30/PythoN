# <----- MULTILEVEL INHERITANCE -----> #
# One Parent class and one child class
# Many levels of Inheritance

class human:
    def __init__(self,name):
        self.name = name
        
class employee(human):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

class IT(employee):
    def __init__(self,name,age,gender):
        super().__init__(name,age)
        self.gender = gender
    def show(self):
        print(f"Name : {self.name}\nAge : {self.age}\nGender : {self.gender}")
        

ch1 = IT("Buddy",10,"Male")
ch1.show()