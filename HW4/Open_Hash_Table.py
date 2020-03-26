#Implement an OPEN hash table with
#hash function hash(i,N)=i%n

class OpenHash:
    def __init__(self,n):
        self.list = [None] * n
        self.idx = 0
        return
    
    def __str__(self):
        for row in self.list:
            if row is None:
                print("Row", self.idx, "[]")
            else:
                print("Row " + str(self.idx) + " " + str(row))
            self.idx =  self.idx + 1
        self.idx = 0
        return ""
    
    def hash(self,i):
        return i % len(self.list)
    
    def insert(self,num):
        if self.member(num) is True:
            return
        else: 
            if self.list[self.hash(num)] is None:
                self.list[self.hash(num)] = [num]
            else:
                self.list[self.hash(num)].append(num)
            return
    
    def member(self,num):
        for row in self.list:
            if row is not None:
                for element in row:
                    if element == num:
                        return True
        return False
    
    def delete(self,num):
        for row in self.list:
            if row is not None:
                for element in row:
                    if element == num:
                        self.list[self.idx].remove(num)
            self.idx = self.idx + 1
        
        self.idx = 0
        return