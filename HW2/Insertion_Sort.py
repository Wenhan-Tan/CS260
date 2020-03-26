def InsertionSort(A):
    #Complete Implementation of this function
    size = len(A)
    i = 0
    j = 0
    for i in range(1, size):
        j = i
        print("Compare", A[j - 1], "to", A[j])
        while (j > 0 and A[j] < A[j - 1]):
            temp = A[j]
            A[j] = A[j - 1]
            A[j - 1] = temp
            j = j - 1
            if j > 0:
                print("Compare", A[j - 1], "to", A[j])
        
    return
#You may add helper functions to this file

#Test Area - Do Not make changes below this line.
import random
print("Insertion Sort Test Question")
x = int(input("Enter Seed for Testing:\n"))
random.seed(x)
test_size = int(input("Enter Test Size:\n"))
L = [random.randint(0,50) for x in range(0,test_size)]

print("Insertion Sorting List")
print("Initial List:",L)
InsertionSort(L)
print("Final List:",L)
