#Implement an Closed hash table with
#hash function hash(i,N)=i mod n
#Rehash Strategy: rehash(i,k,N)= (hash(i,N)+k) mod N

class ClosedHash:
    def __init__(self,n):
        self.list = [None] * n
        self.idx = 0
        return
    
    def __str__(self):
        for row in self.list:
            if row is None:
                print("Row", self.idx, "None")
            else:
                print("Row " + str(self.idx) + " " + str(row))
            self.idx = self.idx + 1
        self.idx = 0
        return ""
        
    def hash(self,i):
        return i % len(self.list)
        
    def rehash(self,i,k):
        return (self.hash(i) + k) % len(self.list)
    
    def insert(self,num):
        self.idx = self.hash(num) % len(self.list)
        if self.member(num) is False:
            for row in self.list:
                if self.list[self.idx] is None:
                    self.list[self.idx] = num
                    break
                else:
                    self.idx = (self.idx + 1) % len(self.list)
        self.idx = 0
        return
    
    def member(self,num):
        for row in self.list:
            if row is not None:
                if row == num:
                    return True
        return False
    
    def delete(self,num):
        self.idx = self.hash(num) % len(self.list)
        for row in self.list:
            if self.list[self.idx] == num:
                self.list[self.idx] = None
            self.idx = (self.idx + 1) % len(self.list)
        self.idx = 0
        return
            