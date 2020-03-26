#Complete this class definition

#It is recommended you create a node class and additional methods

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None
        self.cur = None
        self.node = None
        return
    
    def __str__(self):
        if self.root is None:
            return "Empty Tree"
        else:
            print("Preorder: ", end = "")
            self.preOrder(self.root)
            print("")
            
            print("Inorder: ", end = "")
            self.inOrder(self.root)
            print("")
            
            print("Postorder: ", end = "")
            self.postOrder(self.root)
        return ""
    
    def preOrder(self, root):
        if root is None:
            print("N", end = " ")
            return
        else:
            print(root.value, end = " ")
            self.preOrder(root.left)
            self.preOrder(root.right)
    
    def inOrder(self, root):
        if root is None:
            print("N", end = " ")
            return
        else:
            self.inOrder(root.left)
            print(root.value, end = " ")
            self.inOrder(root.right)
    
    def postOrder(self, root):
        if root is None:
            print("N", end = " ")
            return
        else:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.value, end = " ")
    
    def insert(self, x):
        self.node = Node(x)
        if self.root is None:
            self.root = self.node
            self.node.left = None
            self.node.right = None
        elif self.find(x) is False:
            self.cur = self.root
            while self.cur is not None:
                if x < self.cur.value:
                    if self.cur.left is None:
                        self.cur.left = self.node
                        self.cur = None
                    else:
                        self.cur = self.cur.left
                else:
                    if self.cur.right is None:
                        self.cur.right = self.node
                        self.cur = None
                    else:
                        self.cur = self.cur.right
            self.node.left = None
            self.node.right = None
        return
    
    def find(self,x):
        self.cur = self.root
        while self.cur is not None:
            if x == self.cur.value:
                return True
            elif x < self.cur.value:
                self.cur = self.cur.left
            else:
                self.cur = self.cur.right
        return False
        return