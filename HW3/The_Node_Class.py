#Complete Implementation of this class
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


