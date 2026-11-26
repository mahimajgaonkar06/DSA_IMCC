class Node:
    def __init__(self, value):
        self.left=None
        self.data=value
        self.right=None
class BST:
    def __init__(self):
        self.root=None
        
    def insert(self, new_node):
        if self.root is None: ##BST is empty
            self.root=new_node
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data: #left subtree
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else: #right subree
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right
    
    def get_successor(self,temp):
        temp=temp.right
        while temp is not None and temp.left is not None:
            temp=temp.left
        return temp
  
    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            self.inorder(rt.right)

    def level_order(Self,rt):
        if rt is None:
            print("BST is empty")
        arr=[]
        cnt=0
        arr.append(rt)
        while(cnt<len(arr)):
            temp=arr[cnt]
            cnt+=1
            print(temp.data,end=" ")
            if temp.left:
                arr.append(temp.left)
            if temp.right:
                arr.append(temp.right)


    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)
    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")

    def search(self,key):
        temp=self.root
        while temp:
            if temp.data==key:
                return True
            elif key<temp.data:
                temp=temp.left
            else:
                temp=temp.right

        return False
    def findminmax(self):
        temp=self.root
        while temp.left:
            temp=temp.left
        print("\nMin: ", temp.data)
        temp=self.root
        while temp.right:
            temp=temp.right
        print("\nMax: ", temp.data)

    

b1=BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(6))
b1.insert(Node(65))
b1.insert(Node(300))
b1.insert(Node(500))
b1.insert(Node(50))
print("\nInorder: ")
b1.inorder(b1.root)

print("\n Level order: ")
b1.level_order(b1.root)
