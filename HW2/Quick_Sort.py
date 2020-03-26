import math

def QuickSort(A):
    qsort(A,0,len(A)-1)
    
def qsort(A,start,stop):
    #Implement this function
    if start < stop:
        p = partition(A, start, stop)
        qsort(A, start, p - 1)
        qsort(A, p + 1, stop)
    # j = 0
    # if start >= stop:
    #     return
    
    # j = partition(A, start, stop)
    # qsort(A, start, j - 1)
    # qsort(A, j + 1, stop)
    
def partition(A,start,stop):
    #Implement this function
    pivot = A[stop]
    i = start
    for j in range(start, stop):
        print("Compare", A[j], "to", pivot)
        if A[j] <= pivot:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i = i + 1
    
    temp = A[i]
    A[i] = A[stop]
    A[stop] = temp
    
    return i
    # l = 0
    # h = 0
    # midpoint = 0
    # pivot = 0
    # temp = 0
    # done = False
    
    # midpoint = stop #start + math.floor((stop - start) / 2)
    # pivot = A[midpoint]
    
    # l = start
    # h = stop
    
    # while not done:
    #     # if A[l] > pivot:
    #     #     print("Compare", A[l], "to", pivot)
            
    #     while A[l] < pivot:
    #         # print("Compare", A[l], "to", pivot)    
    #         l = l + 1
        
    #     # if pivot > A[h]:
    #     #     print("Compare", pivot, "to", A[h])
            
    #     while pivot < A[h]:
    #         print("Compare", A[h], "to", pivot)
    #         h = h - 1
        
    #     if l >= h:
    #         done = True
    #     else:
    #         temp = A[l]
    #         A[l] = A[h]
    #         A[h] = temp
            
    #         l = l + 1
    #         h = h - 1
    
    # return h
    
#You may implement helper functions

#Test Area - Do not edit below this line
import random
print("Quick Sort Test Question")
x = int(input("Enter Seed for Testing:\n"))
random.seed(x)
test_size = int(input("Enter Test Size:\n"))
L = [random.randint(0,50) for x in range(0,test_size)]

print("Quick Sorting List")
print("Initial List:",L)
QuickSort(L)
print("Final List:",L)
