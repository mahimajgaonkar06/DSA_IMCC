# class Node:
#     def __init__(self,num):
#         self.num=num
#         self.adr=None

# #giving data to node
# n1=Node(10)
# n2=Node(20)
# n3=Node(40)
# # building connection
# n1.adr=n2
# n2.adr=n3

# # inserting at first pos
# head=n1
# new_node=Node(50)
# new_node.adr=head
# head=new_node
# current=head

# while current is not None:
#     print(current.num)
#     current=current.adr
# print("end")

# # print("delete from start")

# # if head is not None:
# #     head=head.adr

# # # printing
# # current=head
# # while current is not None:
# #     print(current.num)
# #     current=current.adr
# # print("none")

# # print("delete from end")

# # current=head
# # while current.adr.adr is not None:
# #     current=current.adr
# # current.adr=None
# # # printing
# # current=head
# # while current is not None:
# #     print(current.num)
# #     current=current.adr
# # print("none")


# print("delete from position")

# current=head
# while current.adr.num!=20:
#     current=current.adr
# current.adr=current.adr.adr

# # printing
# current=head
# while current is not None:
#     print(current.num)
#     current=current.adr
# print("none")

# print("reversing list")
# last=None
# current=head

# while current is not None:
#     next_node=current.adr
#     current.adr=last
#     last=current
#     current=next_node
# head=last


# # # travesing the list

# # head=n1
# # current=head

# # while current is not None:
# #     print(current.num)
# #     current=current.adr
# # print("none")



# # printing
# current=head
# while current is not None:
#     print(current.num)
#     current=current.adr
# print("none")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(3)
b = Node(6)
a.next = b
b.next = a

print(a.next.next.data)