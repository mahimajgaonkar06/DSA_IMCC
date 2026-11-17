class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class cQueue:
    def __init__(self):
        self.front=None
        self.rear=None


    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
        self.rear.next=self.front # added for circular

    def dequeue(self):
        if self.front:
            temp=self.front
            
        
            if self.front==self.rear:#updated for cqueue
                self.front=self.rear=None
                print("now empty")
                return
            else:
                self.front =self.front.next
            
                self.rear.next=self.front #this too
            temp=None
            
        else:
            print('queue is empty')


    def print(self):
        temp=self.front
        while True:
            print(temp.data)
            temp=temp.next
            if temp==self.front:
                break
        

        
q1=cQueue()
q1.enqueue(Node(10))
q1.enqueue(Node(20))
q1.enqueue(Node(50))
q1.print()
q1.dequeue()
q1.dequeue()
print("dequeue")
q1.print()
q1.enqueue(Node(40))
print("circular")
q1.print()