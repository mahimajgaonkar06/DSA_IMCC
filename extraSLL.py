class Node:
    def __init__(self,num):
        self.num=num
        self.adr=None

#giving data to node
n1=Node(10)
n2=Node(20)
n3=Node(40)
# building connection
n1.adr=n2
n2.adr=n3

# inserting at first pos
head=n1
new_node=Node(50)
new_node.adr=head
head=new_node
current=head

while current is not None:
    print(current.num)
    current=current.adr
print("end")


# # travesing the list

# head=n1
# current=head

# while current is not None:
#     print(current.num)
#     current=current.adr
# print("none")








# # printing
# current=n1
# while current is not None:
#     print(current.num)
#     current=current.adr
# print("none")
