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

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.temp = None
        self.result = []
        self.size = 0
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
        self.size = self.size + 1
        if self.empty():
            self.head = Node(x, None)
            self.tail = self.head
        else:
            self.tail.setNext(Node(x, None))
            self.tail = self.tail.getNext()
        return 
    
    def dequeue(self):
        self.size = self.size - 1
        self.temp = self.head
        self.head = self.head.next
        return self.temp.getValue()

if __name__ == '__main__':
    print("The Josephus Problem")
    numPeople = int(input("Enter the Number of People in the Group:\n"))
    mthPerson = int(input("Enter value for Mth Person to be killed:\n"))
    Q = Queue()
    
    for i in range(0, numPeople):
        Q.enqueue(i)
    
    result = []
    print("Order in which people are killed:")
    for i in range(0, numPeople):
        for j in range(0, mthPerson - 1):
            value = Q.dequeue()
            Q.enqueue(value)
            
        result.append(Q.dequeue())
    print(' '.join(str(x) for x in result))
        
        
    