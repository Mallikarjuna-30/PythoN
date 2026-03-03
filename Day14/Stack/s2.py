#<----- Stack using Class ----->#

class stack:
    def __init__(self):
        self.stack = []
    
    def push(self,value):
        self.stack.append(value)
        
    def pop(self):
        if self.is_empty()==False:
            return self.stack.pop()
        return "Stack is empty"
    
    def peek(self):
        if self.is_empty()==False:
            return self.stack[-1]
        return("Stack is empty")
    
    def is_empty(self):
        return len(self.stack) == 0
    
s = stack()
s.push(10)
s.push(20)
s.push(30)
n = s.peek()
print(n)
print(s.pop())
