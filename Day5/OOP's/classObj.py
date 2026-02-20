# <-----Class and Object-----> #

# Class is a blueprint for creating objects
# Object is an instance of a class

# class bottle:
#     material = "plastic"      #attributes
#     color = "blue"
#     size = "medium"
#     def drink(self):            #methods
#         print("Drinking water from the bottle")
        

# # Creating objects
# b1 = bottle()

# # Accessing attributes
# print(b1.material)
# print(bottle().color)

# # Accessing methods
# b1.drink()
# bottle().drink()

class Std:
    schoolname = "DPS"                        #class attributes
    def __init__(self,name,course,age=18):         # self => is used to access the attributes of the current class
        self.name = name                    #instance attributes
        self.course = course
        self.age = age

    def infomt(self):                         #instance method => here self refers to the current object
        print(self.name,self.course,self.age)
        
    @classmethod
    def info(cls):
        print(cls.schoolname)
    @staticmethod
    def show():
        print("This is a static method")
        
Std("Mallu","Python",20).infomt()
Std.show()
s1 = Std("Malli","Java")
s1.info()


# Types of methods
# Instance method => works with instance of the class
# Class method => we use @classmethod decorator
# Static method => we use @staticmethod decorator

