# Comapny wants to caculate the salary of employee
# Each employeee has name , id
# types of employees  => Full time , Part time , Intern

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class FullTime(Employee):
    def __init__(self,name,id,salary):
        super().__init__(name,id)
        self.salary = salary
        
    def show(self):
        print(f"Name : {self.name}")
        print(f"ID : {self.id}")
        print(f"Salary : {self.salary}")
        
class partTime(Employee):
    def __init__(self,name,id,hours,salary):
        super().__init__(name,id)
        self.hours = hours
        self.salary = salary
    
    def show(self):
        tsalary = self.hours * self.salary
        print(f"Name : {self.name}")
        print(f"ID : {self.id}")
        print(f"Total Salary : {tsalary}")

class Intern(Employee):
    def __init__(self,name,id,stipend):
        super().__init__(name,id)
        self.stipend = stipend
    
    def show(self):
        print(f"Name : {self.name}")
        print(f"ID : {self.id}")
        print(f"Total Salary : {self.stipend}")
        
n = int(input("Enter number of employees (Fulltime/Parttime/Intern): "))
for i in range(n):
    typee = input("Enter the type of employee : ").lower()
    if(typee == "fulltime"):
        name = input("Enter name : ")
        id = int(input("Enter id : "))
        salary = int(input("Enter salary : "))
        f = FullTime(name,id,salary)
        print("\n")
    elif(typee == "parttime"):
        name = input("Enter name : ")
        id = int(input("Enter id : "))
        hours = int(input("Enter hours : "))
        salary = int(input("Enter salary : "))
        p = partTime(name,id,hours,salary)
        print("\n")
    elif(typee == "intern"):
        name = input("Enter name : ")
        id = int(input("Enter id : "))
        stipend = int(input("Enter stipend : "))
        i = Intern(name,id,stipend)
        print("\n")
    else:
        print("Invalid type")
        print("\n")
        
for i in range(n):
    if(typee == "fulltime"):
        f.show()
        print("\n")
    elif(typee == "parttime"):
        p.show()
        print("\n")
    elif(typee == "intern"):
        i.show()
        print("\n")