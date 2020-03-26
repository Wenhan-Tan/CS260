import math

def MergeSort(A):
    msort(A,0,len(A)-1) 
    
def msort(A,start,stop):
    #Complete Implementation
    j = 0
    if start < stop:
        j = math.floor((start + stop) / 2)
        
        msort(A, start, j)
        msort(A, j + 1, stop)
        
        merge(A, start, j, stop)

def merge(A,start,middle,stop):
    #Complete Implementation
    mergedSize = stop - start + 1
    mergePos = 0
    leftPos = 0
    rightPos = 0
    mergedNumbers = [None] * mergedSize
    
    leftPos = start
    rightPos = middle + 1
    
    while (leftPos <= middle) and (rightPos <= stop):
        print("Compare", A[rightPos], "to", A[leftPos])
        if A[leftPos] < A[rightPos]:
            mergedNumbers[mergePos] = A[leftPos]
            leftPos = leftPos + 1
        else:
            mergedNumbers[mergePos] = A[rightPos]
            rightPos = rightPos + 1
        
        mergePos = mergePos + 1
    
    while leftPos <= middle:
        mergedNumbers[mergePos] = A[leftPos]
        leftPos = leftPos + 1
        mergePos = mergePos + 1
    
    while rightPos <= stop:
        mergedNumbers[mergePos] = A[rightPos]
        rightPos = rightPos + 1
        mergePos = mergePos + 1
    
    for mergePos in range(0, mergedSize):
        A[start + mergePos] = mergedNumbers[mergePos]

#You may add additional helper functions


#Test Area - Do not make changes below this line
import random
print("Merge Sort Test Question")
x = int(input("Enter Seed for Testing:\n"))
random.seed(x)
test_size = int(input("Enter Test Size:\n"))
L = [random.randint(0,50) for x in range(0,test_size)]

print("Merge Sorting List")
print("Initial List:",L)
MergeSort(L)
print("Final List:",L)
