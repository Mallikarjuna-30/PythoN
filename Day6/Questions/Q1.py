# School Management System
# A school has => Teachers , Students , Staff
# All have Name , id 
# teacher has salary
# student has marks
# staff has dept
# Marks and salary are private
# Display details of all teachers , students , staff

class school:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class teacher(school):
    def __init__(self,name,id,salary):
        super().__init__(name,id)
        self.__salary = salary
    
    # def set_salary(self,salary):
    #     self.__salary = salary
        
    # def get_salary(self):
    #     return self.__salary

    def show(self):
        print(f"Name : {self.name}")
        print(f"ID : {self.id}")
        print(f"Salary : {self.__salary}")

class student(school):
    def __init__(self,name,id,marks):
        super().__init__(name,id)
        self.__marks = marks
    
    def set_marks(self,value):
        if(0< value <=100):
            self.__marks = value
        else:
            print("Invalid marks")
    
    # def get_marks(self):
    #     return self.__marks
    
    def show(self):
        print(f"Name : {self.name}")
        print(f"ID : {self.id}")
        print(f"Marks : {self.__marks}")

class staff(school):
    def __init__(self,name,id,dept):
        super().__init__(name,id)
        self.dept = dept
    
    # def set_dept(self,dept):
    #     self.dept = dept
    
    # def get_dept(self):
    #     return self.dept
    
    def show(self):
        print(f"Name : {self.name}")
        print(f"ID : {self.id}")
        print(f"Department : {self.dept}")
        
tn = int(input("Enter number of teachers : "))
for i in range(tn):
    print("Enter teacher details")
    name = input("Enter name Teacher : ")
    id = int(input("Enter id Teacher : "))
    salary = int(input("Enter salary Teacher : "))
    t = teacher(name,id,salary)
    print("\n")
    
sn = int(input("Enter number of students : "))
for i in range(sn):
    print("Enter student details")
    name = input("Enter name Student : ")
    id = int(input("Enter id Student : "))
    marks = int(input("Enter marks Student : "))
    s = student(name,id,marks)
    print("\n")
    
stn = int(input("Enter number of staff : "))
for i in range(stn):
    print("Enter staff details")
    name = input("Enter name Staff : ")
    id = int(input("Enter id Staff : "))
    dept = input("Enter department Staff : ")
    st = staff(name,id,dept)
    print("\n")
    
for i in range(tn):
    print("Teacher details are: ")
    t.show()
    print("\n")
    
for i in range(sn):
    print("Student details are: ")
    s.show()
    print("\n")
    
for i in range(stn):
    print("Staff details are: ")
    st.show()