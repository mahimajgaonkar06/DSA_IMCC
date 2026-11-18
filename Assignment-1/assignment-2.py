class Node:
    def __init__(self, pid, name, pr):
        self.pid = pid
        self.name = name
        self.priority = pr
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None
        self.size = 0

    #1. Add Process
    def enqueue(self, new_node):
        if new_node.priority not in (1, 2, 3, 4):
            print("Invalid priority(priority must be from 1 to 4)")
            return
        # if queue is empty or new priority is less than old priority
        if self.front is None or new_node.priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            temp = self.front
            # keep traversing until the priority of next process becomes 
            # lesser or equal to the new process
            while temp.next and temp.next.priority <= new_node.priority:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

        self.size += 1
        print("Process Added:", new_node.pid, new_node.name)

    # 2.Execute Process(removing the process from queue that are completed)
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        print("Executing Process:", temp.pid, "-", temp.name,
              "(priority)", temp.priority)
        self.front = self.front.next
        self.size -= 1

    # 3. View Next Process
    def display_next(self):
        if self.front is None:
            print("Queue is empty")
            return
        print("Next Process:", self.front.pid, "-", self.front.name,
              "(Priority)", self.front.priority)

    # 4. Display Processes
    def display_all(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        while temp:
            print("process id: ",temp.pid, " Process Name: ", temp.name, " (priority)", temp.priority)
            temp = temp.next

    # 5. Count Processes (count)
    def count(self):
        print("Total pending processes:", self.size)



# creating priority queue
pq = PriorityQueue()

pq.enqueue(Node(10, "Chrome", 2))
pq.enqueue(Node(20, "File Manager", 1))
pq.enqueue(Node(30, "Email", 3))
pq.enqueue(Node(40, "Music Player", 4))
pq.enqueue(Node(50, "Text Editor", 2))
pq.enqueue(Node(60, "Video Player", 4))
pq.enqueue(Node(70, "Image Viewer", 1))


print("\n--- All Processes ---")
pq.display_all()

print("\n--- Next Process ---")
pq.display_next()

print()
pq.count()

print("\n--- Executing ---")
pq.dequeue()
pq.dequeue()

print("\n--- Remaining ---")
pq.display_all()
pq.count()

pq.dequeue()
pq.dequeue()
pq.dequeue()
pq.dequeue()  # empty queue check