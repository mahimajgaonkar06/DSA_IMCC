class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def create(self,new_node):
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node
    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    

list1=LinkedList()
n1=Node(10)
n2=Node(20)
list1.create(n1)
list1.create(n2)
list1.create(Node(30))
list1.print()
