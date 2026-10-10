class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            p = 1
            temp = self.head
            while p != pos - 1:
                temp = temp.next
                p += 1
            new_node.next = temp.next
            temp.next = new_node

    def delete(self, value):
        temp = self.head
        prev = None

        if temp == None:
            print("List is empty")
            return

        if temp.data == value:
            self.head = temp.next
        else:
            while temp and temp.data != value:
                prev = temp
                temp = temp.next

            if temp == None:
                print("Value not present")
                return

            prev.next = temp.next
            temp = None

    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow:
            print(slow.data)

    def reverse(self):
        prev = None
        temp = self.head

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.head = prev

    def consecutive_sum(self):
        temp = self.head

        while temp and temp.next:
            print("sum: ",temp.data + temp.next.data)
            temp = temp.next

    def print(self):
        temp = self.head

        while temp:
            print("displaying: ",temp.data)
            temp = temp.next


list1 = LinkedList()

n1 = Node(10)
n2 = Node(20)

list1.create(n1)
list1.create(n2)
list1.create(Node(30))

list1.insert(Node(53), 3)

list1.delete(65)

list1.middle()
list1.reverse()
list1.print()
list1.consecutive_sum()
list1.print()
