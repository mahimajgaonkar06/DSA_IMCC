class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
    def print(self):
        temp=self.front
        while temp:
            print(temp.data)
            temp=temp.next
        
q1=Queue()
q1.enqueue(Node(10))
q1.enqueue(Node(20))
q1.enqueue(Node(50))
q1.print()