# <----- POLYMORPHISM -----> #
# <----- OVERRIDING -----> #

class animal:
    def sound(self):
        print("Animal makes sound")

# class dog(animal):
#     def sound(self):
#         print("Dog barks")

class human(animal):
    def sound(self):
        print("Human makes sound")
        
# o = animal()
# o.sound()
obj = human()
obj.sound()