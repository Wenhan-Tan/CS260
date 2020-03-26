import math

def T(n):
    if n <= 1:
        return 1
    else:
        return a * T(math.floor(n/b)) + (n ** x) * math.ceil(math.log2(n) ** y)

if __name__ == "__main__":
    print("General Recursion Example")
    a = int(input("Enter Value for a:\n"))
    b = int(input("Enter Value for b:\n"))
    x = int(input("Enter Value for x:\n"))
    y = int(input("Enter Value for y:\n"))
    n = int(input("Enter Value for n:\n"))
    output = T(n)
    
    print("Evaluating " + str(a) + "T(n/" + str(b) + ")+n^" + str(x) + " log2(n)^" + str(y))
    print("T(" + str(n) + ")=" + str(output))