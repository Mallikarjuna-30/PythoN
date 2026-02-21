class student:
    def __init__(self):
        self.__marks = 0
    
    def set_mark(self,value):
        if(0< value <=100):
            self.__marks = value
        else:
            print("Invalid marks")
        
    def get_marks(self):
        return self.__marks
        
obj = student() 
m = int(input("Enter marks : "))
obj.set_mark(m)
print(obj.get_marks())
