#<-----Deletion Operations---->#
from LL1 import insert_end 
from LL1 import insert_pos 
from LL1 import insert_beg 

class Node:
    def __init__(self,data):           #Structure of node
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None                #Creation of Linkedlist
        
    def del_beg(self):
        if self.head == None:
            print("empty list")
            return
        self.head = self.head.next
    
    def del_end(self):
        if self.head == None:
            print("List is empty")
            return
        temp = self.head
        while temp.right != None:
            pre = temp
            temp = temp.next
        pre.next = None
        
        
l = Linkedlist()
l.insert_end(10)
l.insert_end(20)
l.insert_end(30)
l.insert_beg(5)
l.insert_pos(15,1)
l.del_beg()
l.display()