#Complete Implementation of this file

#Copy in your Node Class from the previous question.

#You MUST implement using your node class
class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next
        self.last = None
        self.temp = None
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
    
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.temp = None
        self.result = []
        return
    
    def __str__(self):
        self.temp = self.head
        if self.head is None:
            return "Queue Empty"
        else:
            while self.temp is not None:
                self.result.append(str(self.temp))
                self.temp = self.temp.next
            return ''.join(self.result)
            
    def front(self):
        return self.head.getValue()
        
    def empty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def enqueue(self,x):
        if self.empty():
            self.head = Node(x, None)
            self.tail = self.head
        else:
            self.tail.setNext(Node(x, None))
            self.tail = self.tail.getNext()
        return 
    
    def dequeue(self):            
        self.head = self.head.next
        return
