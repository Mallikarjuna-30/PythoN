

class Bags:
    def __init__(self,name,price,color):
        self.name = name
        self.price = price
        self.color = color
    
    def show(self):
        print(f"Name : {self.name}")
        print(f"Price : {self.price}")
        print(f"Color : {self.color}")

n = int(input("Enter the number of bags : "))
for i in range(n):
    name = input(f"Enter the name of bag {i+1} : ")
    price = int(input(f"Enter the price of bag {i+1} : "))
    color = input(f"Enter the color of bag {i+1} : ")
    
for i in range(n):
    b=Bags(name,price,color)
    b.show()
