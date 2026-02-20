# <----- INHERITANCE -----> #

# Inheritance is a mechanism in which one class acquires the properties of another class
# Parent class => class from which we inherit a new class ( Old Class )
# Child class => class which inherits ( New Class )

# Single level inheritance => one parent class and one child class



class Animal:           #parent / superclass / base class
    # def __init__(self,name):
    #     self.name = name
    def eat(self):
        print("All Animal eats food...")
        
class Dog(Animal):      #child / subclass / derived class
    def __init__(self,name):
        self.name = name
    def sound(self):
        print(f"{self.name} Dog barks.... ")
        
d1 = Dog("Buddy")
d1.sound()
d1.eat()
