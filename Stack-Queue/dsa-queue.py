class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None

        temp = self.front
        value = temp.data

        self.front = self.front.next

        if self.front is None:
            self.rear = None

        temp.next = None
        return value


    def reverse(self):
        def reverse(self):
            st = []

            while self.front is not None:
                st.append(self.dequeue())

            while len(st) > 0:
                self.enqueue(Node(st.pop()))

    def print(self):
        temp=self.front
        while temp:
            print(temp.data)
            temp=temp.next



# MERGE TWO QUEUES
def merge(q1, q2):
    q3 = Queue()

    temp = q1.front
    while temp:
        q3.enqueue(Node(temp.data))
        temp = temp.next

    temp = q2.front
    while temp:
        q3.enqueue(Node(temp.data))
        temp = temp.next

    return q3


    # CHECK IDENTICAL QUEUES
def identical(q1, q2):
    temp1 = q1.front
    temp2 = q2.front

    while temp1 and temp2:
        if temp1.data != temp2.data:
            print("Queues are not identical")
            return

        temp1 = temp1.next
        temp2 = temp2.next

    if temp1 is None and temp2 is None:
        print("Queues are identical")
    else:
        print("Queues are not identical")

    

q1 = Queue()
q2 = Queue()

q1.enqueue(Node(10))
q1.enqueue(Node(27))
q1.enqueue(Node(78))

q2.enqueue(Node(40))
q2.enqueue(Node(50))
q2.enqueue(Node(34))
q2.enqueue(Node(83))

print("Queue 1:")
q1.print()

print("Queue 2:")
q2.print()

q1.reverse()
print("After reverse:")
q1.print()

q3 = merge(q1, q2)
print("After merging:")
q3.print()

print("Checking identical:")
identical(q1, q2)
