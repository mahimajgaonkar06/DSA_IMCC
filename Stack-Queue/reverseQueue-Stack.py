class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self,new_node):
        new_node.next=self.top
        self.top=new_node
    
            
    def print(self):
        temp=self.top
        print("stack elements: ")
        while temp:
            print(temp.data)
            temp=temp.next

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


    def dequeue(self):
        if self.front:
            temp=self.front
            deq_data=temp.data
            self.front =self.front.next
            if self.front==None:
                self.rear=None
            temp=None
            return deq_data
        else:
            print('queue is empty')

    def is_empty(self):
        return self.front is None

    def print(self):
        temp=self.front
        while temp:
            print(temp.data)
            temp=temp.next

def reverse_queue(q1):
    stk=Stack()
    while not q1.is_empty():
        stk.push(Node(q1.dequeue()))
    stk.print()


q1=Queue()
q1.enqueue(Node(10))
q1.enqueue(Node(20))
q1.enqueue(Node(50))
q1.print()
reverse_queue(q1)

