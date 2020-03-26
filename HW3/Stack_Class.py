#Complete Implementation of this class

#Copy your Node class from the previous problem

#Use your Node Class to Implement a Stack
class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next
        return
    def __str__(self):
        return ("[ " + str(self.value) + " ]")
    def getNext(self):
        return self.next
    def setNext(self,n):
        self.next = n
        return 
    def getValue(self):
        return self.value
    def setValue(self,v):
        self.value = v
        return

class Stack:
    def __init__(self):
        self.head = None
        self.temp = None
        self.result = []
        return
    
    def __str__(self):
        self.temp = self.head
        if self.head is None:
            return "Stack Empty"
        else:
            while self.temp is not None:
                self.result.append(str(self.temp))
                self.temp = self.temp.next
            return ''.join(self.result)
                
    def top(self):
        return self.head.getValue()
    
    def pop(self):
        self.head = self.head.getNext()
        return
    
    def push(self,x):
        if self.empty():
            self.head = Node(x, None)
        else:
            self.temp = self.head
            self.head = Node(x, None)
            self.head.setNext(self.temp)
        return
    
    def empty(self):
        return self.head is None