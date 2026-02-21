# <----- ENCAPSULATION -----> #
# Binding data and functions into a single unit


# _(single underscore) before variables represents protected
# __(double underscore) before variables represents private

# class Factory:
#     a = "Bhopal"                # Public variable
#     _b = "protected variable"   # Protected variable
#     __c = "private variable"    # Private variable
#     def show(self):
#         print("I am in pune factory")
    
#     def show3(self):
#         return self.__c
        
# class Bhopal(Factory):
#     def show2(self):
#         print(f"I am from {super().a} factory")
#         print(f"I am from {super()._b} factory")
#         print(f"I am from {super().show3()}factory")
        
# b = Bhopal()
# b.show2()


class Factory:
    def __init__(self , location):
        self.__location = location
        
    def set_loc(self,loc):          # used to asssign the value to the private variable
        self.__location = loc
    
    def get_loc(self):              # used to get the value of the private variable
        return self.__location
    
obj = Factory("pune")
print(obj.get_loc())
obj.set_loc("mumbai")
print(obj.get_loc())
