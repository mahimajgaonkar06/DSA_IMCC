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
    def pop(self):
        if self.isempty():
            print("empty")
        else:
            temp=self.top
            print("pop element: ",temp.data)
            self.top=self.top.next
            temp=None
            
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
    s1=Stack()
    while not q1.is_empty():
        s1.push(Node(q1.dequeue()))
    s1.print()

def reverse_stack(s1):
    q1=Queue()
    while not s1.is_empty():
        q1.enqueue(Node(s1.pop()))
    q1.print()

q1=Queue()
s1=Stack()
q1.enqueue(Node(10))
q1.enqueue(Node(20))
q1.enqueue(Node(50))
q1.print()
reverse_queue(q1)


st.push(Node(10))
st.push(Node(17))
st.push(Node(23))
st.push(Node(50))
st.push(Node(12))
st.push(Node(19))

reverse_stack(s1)