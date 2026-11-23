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

    # 1. Add Process
    def enqueue(self, new_node):
        if new_node.priority not in (1, 2, 3, 4):
            print("Invalid priority! Use 1 to 4.")
            return

    # this checks if the latest priority is smaller than older or not
        if self.front is None or new_node.priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            temp = self.front
            
            while temp.next and temp.next.priority <= new_node.priority:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

        self.size += 1
        print("Process Added:", new_node.pid, new_node.name)

    # 2. Execute Process
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        print("Executing Process:", temp.pid, "-", temp.name,
              "| Priority:", temp.priority)
        self.front = self.front.next
        self.size -= 1

    # 3. View Next Process
    def display_next(self):
        if self.front is None:
            print("Queue is empty")
            return
        print("Next Process:", self.front.pid, "-", self.front.name,
              "| Priority:", self.front.priority)

    # 4. Display Processes
    def display_all(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        
        while temp:
            print(temp.pid, "\t", temp.name, "\t", temp.priority)
            temp = temp.next

    # 5. Count Processes 
    def count(self):
        print("Total pending processes:", self.size)




pq = PriorityQueue()
# displaying menu for user input
while True:
    print("\n===== CPU Process Scheduling =====")
    print("1. Add Process")
    print("2. Execute Process")
    print("3. View Next Process")
    print("4. Display All Processes")
    print("5. Count Processes")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number between 1 and 6.")
        continue

    if choice == 1:
        try:
            pid = int(input("Enter Process ID: "))
            name = input("Enter Process Name: ")
            pr = int(input("Enter Priority (1-4): "))
            pq.enqueue(Node(pid, name, pr))
        except ValueError:
            print("Invalid input!")
    elif choice == 2:
        pq.dequeue()
    elif choice == 3:
        pq.display_next()
    elif choice == 4:
        pq.display_all()
    elif choice == 5:
        pq.count()
    elif choice == 6:
        print("Exiting program...")
        break
    else:
        # for the menu option selected other 1 to 6
        print("Invalid choice! Try again.")