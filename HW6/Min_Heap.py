#Mark Boady
#CS 260 - Complete Implementation
import math

class heap:
    def __init__(self):
        self.data = []
        
    def __str__(self):
        res=""
        for x in self.data:
            res=res+str(x)+" "
        return res
        
    def makenull(self):
        self.data = []
        return
    
    def insert(self,x):
        self.data.append(x)
        self.upheap(len(self.data) - 1)
        return
    
    def parent(self,index):
        return math.floor((index - 1) / 2)
    
    def left(self,index):
        return (index + 1) * 2 - 1
    
    def right(self,index):
        return (index + 1) * 2
    
    def swap(self,a,b):
        temp = self.data[a]
        self.data[a] = self.data[b]
        self.data[b] = temp
        return
    
    def upheap(self,index):
        if (self.parent(index) < 0):
            return
        
        temp = self.data[self.parent(index)]
        
        if temp <= self.data[index]:
            return
        
        self.swap(index, self.parent(index))
        self.upheap(self.parent(index))
        return
    
    def inorder(self,index):
        if index < len(self.data):
            self.inorder(self.left(index))
            print(self.data[index], end = " ")
            self.inorder(self.right(index))
        return ""
    
    def preorder(self,index):
        if index < len(self.data):
            print(self.data[index], end = " ")
            self.preorder(self.left(index))
            self.preorder(self.right(index))
        return ""
    
    def postorder(self,index):
        if index < len(self.data):
            self.postorder(self.left(index))
            self.postorder(self.right(index))
            print(self.data[index], end = " ")
        return ""
    
    def min(self):
        return self.data[0]
    
    def deletemin(self):
        self.swap(0, (len(self.data) - 1))
        self.data.pop(len(self.data) - 1)
        self.downheap(0)
        return
    
    def downheap(self,index):
        # for j in self.data:
        #     print(j)
        # print("Done")
        
        if (self.left(index) >= len(self.data)) and (self.right(index) >= len(self.data)):
            return
        
        if (self.left(index) < len(self.data)) and (self.right(index) < len(self.data)):
            if self.data[index] <= self.data[self.left(index)] and self.data[index] <= self.data[self.right(index)]:
                return
        
        if (self.left(index) < len(self.data)) and (self.right(index) < len(self.data)):
            if self.data[self.left(index)] <= self.data[self.right(index)]:
                self.swap(index, self.left(index))
                self.downheap(self.left(index))
            else:
                self.swap(index, self.right(index))
                self.downheap(self.right(index))
        
        if (self.left(index) >= len(self.data)):
            if self.data[index] > self.data[self.right(index)]:
                self.swap(index, self.right(index))
                self.downheap(self.right(index))
        
        if (self.right(index) >= len(self.data)):
            if self.data[index] > self.data[self.left(index)]:
                self.swap(index, self.left(index))
                self.downheap(self.left(index))
        
        return
    
    def sort(self):
        for i in range(0, len(self.data)):
            print(self.data[0])
            self.swap(0, len(self.data) - 1)
            self.data.pop(len(self.data) - 1)
            if (len(self.data) > 1):
                 self.downheap(0)

        # print(self.data[0])
            
        return