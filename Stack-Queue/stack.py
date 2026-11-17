class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
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
    def reverse(self):
        temp=self.top 
        while temp:
            st1.push(Node(temp.data))
            temp=temp.next
            
    def print(self):
        temp=self.top
        print("stack elements: ")
        while temp:
            print(temp.data)
            temp=temp.next

st=Stack()
st1=Stack()
st.push(Node(10))
st.push(Node(17))
st.push(Node(23))
st.push(Node(50))
st.push(Node(12))
st.push(Node(19))
st.print()
st.pop()
st.print()
st.reverse()
st1.print()
