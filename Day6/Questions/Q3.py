# Building a payment system for e-commerce website
# Different payment methods => UPI , Card
# Sensitive details must be hidden like pin and cvv

class payment:
    def __init__(self,name, amount):
        self.name = name
        self.amount = amount
    
    def pay(self):
        print(f"Name : {self.name}")
        print(f"Amount : {self.amount}")

class UPI(payment):
    def __init__(self,name,amount,pin):
        super().__init__(name,amount)
        self.__pin = pin
        
    def pay(self):
        print(f"Name : {self.name}")
        print(f"Amount : {self.amount}")
        print(f"Pin : Hidden")

class Card(payment):
    def __init__(self,name,amount,cvv):
        super().__init__(name,amount)
        self.__cvv = cvv
        
    def pay(self):
        print(f"Name : {self.name}")
        print(f"Amount : {self.amount}")
        print(f"CVV : Hidden")
        
n = int(input("Enter number of payments : "))
for i in range(n):
    type = input("Enter the type of payment : ").lower()
    if(type == "upi"):
        name = input("Enter name : ")
        amount = int(input("Enter amount : "))
        pin = int(input("Enter pin : "))
        u = UPI(name,amount,pin)
        print("\n")
    elif(type == "card"):
        name = input("Enter name : ")
        amount = int(input("Enter amount : "))
        cvv = int(input("Enter cvv : "))
        c = Card(name,amount,cvv)
        print("\n")
    else:
        print("Invalid type")
        print("\n")
        
for i in range(n):
    if(type == "upi"):
        u.pay()
        print("\n")
    elif(type == "card"):
        c.pay()
        print("\n")