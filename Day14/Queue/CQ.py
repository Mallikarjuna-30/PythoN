#<----- Circular Queue ----->#

class circularQueue:
    def __init__(self,size):
        self.size = size
        self.queue = [None]*size
        self.f = -1
        self.r = -1
        
    def enqueue(self,data):
        if(self.f == (self.r+1)%self.size):
            print("Queue is full")
            return
        
        if self.f == -1:
            self.f =0
            self.r = 0
            
        else:
            self.r = (self.r + 1)%self.size
        
        self.queue[self.r] = data
        print("Inserted an element")
        
    def dequeue(self):
        if self.f == -1:
            print("Queue is empty")
            return
        
        removed = self.queue[self.f]
        self.queue[self.f] = None
        
        if self.f == self.r:
            self.f = -1
            self.r = -1
        else:
            self.f = (self.f +1)%self.size
            
        print("\nThe removed element is ",removed)
        
    def display(self):
        print("The elements are: ")
        i = self.f
        while True:
            print(self.queue[i],end = " ")
            if i == self.r:
                break
            i = (i + 1)% self.size
            
        
        
c = circularQueue(3)
c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
c.display()
c.dequeue()
c.display()