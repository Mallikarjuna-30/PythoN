#<----- Double Linked List ----->#
#                   [ Left | Data | Right ]

class Node:
    def __init__(self,data):           #Structure of node
        self.data = data
        self.right = None
        self.left = None
        
class Linkedlist:
    def __init__(self):
        self.head = None                #Creation of Linkedlist
        
    def insert_beg(self , data):
        new_node = Node(data)
        new_node.right = self.head
        new_node.left = None
        self.head = new_node
        
    def insert_end(self,data):
        new_node = Node(data)
        
        if  self.head == None:
            self.head = new_node
            return
        temp = self.head
        
        while temp.right != None:
            temp = temp.right
        temp.right = new_node
        
    def insert_pos(self,data,pos):
        if pos < 1:
            print("Invalid pos")
            return 
        new_node = Node(data)
        
        if pos == 1:
            l.insert_beg(data)
            return
        temp = self.head
        
        for i in range(pos-2):
            if temp == None or temp.next == None:
                print("Invalid position")
                return
            temp = temp.right
        new_node.right = temp.right
        temp.right = new_node
        
    def del_beg(self):
        if self.head == None:
            print("List is empty")
            return
        self.head = self.head.right
        
    def del_end(self):
        if self.head == None:
            print("List is empty")
            return
        temp = self.head
        
        while temp.right != None:
            pre = temp
            temp = temp.right
        pre.right = None
        temp.left = None
        
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data,end="->")
            temp = temp.right
        print("None")
        
        
l = Linkedlist()
l.insert_end(10)
l.insert_end(20)
l.insert_end(30)
l.insert_beg(5)
l.insert_beg(9)
l.insert_pos(15,1)
l.display()
l.del_beg()
l.del_end()
l.display()