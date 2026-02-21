class animal:
    def __init__(self,name):
        self.name=name
    age = 10
        
class dog(animal):
    def __init__(self,name):
        super().__init__(name)
        
    def sound(self):
        print(f"{self.name} Dog barks.... ")
        print(super().age)
        
d1 = dog("Buddy")
d1.sound()