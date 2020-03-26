def BubbleSort(A):
    #Complete Implementation
    size = len(A)
    check = 0
    while check != size - 1:
        check = 0
        idx = 0
        for i in range(0, size - 1):
            print("Compare", A[idx], "to", A[idx+1])
            if A[idx] > A[idx + 1]:
                temp = A[idx]
                A[idx] = A[idx + 1]
                A[idx + 1] = temp
            else:
                check = check + 1
            idx = idx + 1
    # for i in range(0, size - 1):
    #     for j in range(0, size - i - 1):
    #         print("Compare", A[j], "to", A[j+1])
    #         if A[j] > A[j+1]:
    #             temp = A[j]
    #             A[j] = A[j+1]
    #             A[j + 1] = temp
                
    return
#You may implement helper functions

#Test Area - Do Not make changes below this line.
import random
print("Bubble Sort Test Question")
x = int(input("Enter Seed for Testing:\n"))
random.seed(x)
test_size = int(input("Enter Test Size:\n"))
L = [random.randint(0,50) for x in range(0,test_size)]

print("Bubble Sorting List")
print("Initial List:",L)
BubbleSort(L)
print("Final List:",L)