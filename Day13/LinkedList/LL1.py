#<---- Linked List ---->#
# Linked List ==> it is a collection of nodes , where is node has two parts (data , link to next node)
#                                  [ DATA | LINK ] 
# Types => Single,Doubly,Circular,doubly Circular LL
# Operations => Insertion , Deletion

class Node:
    def __init__(self,data):           #Structure of node
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None                #Creation of Linkedlist
    
    # Insertion at Beginning
    def insert_beg(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Insertion at End
    def insert_end(self,data):
        new_node = Node(data)
    
        if self.head == None:
            self.head = new_node
            return
    
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
        
    # Insertion at Specific Position
    def insert_pos(self,data,pos):
        if pos < 1:
            print("Invalid Position")
            return
        
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        
        temp = self.head
        for i in range(pos-2):
            if temp == None or temp.next == None:
                print("Invalid Position")
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data,end="->")
            temp = temp.next
        print("None")


l = Linkedlist()
l.insert_end(10)
l.insert_end(20)
l.insert_end(30)
l.insert_beg(5)
l.insert_pos(15,1)
l.display()