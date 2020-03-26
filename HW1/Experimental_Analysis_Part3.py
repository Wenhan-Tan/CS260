import math

def T(n):
    if n == 1:
        return 1
    
    Tn = T(n/2) + 1
    
    return Tn

print("Analysis of Second Recursive Function")
print("Enter starting power of 2:")
startPower = int(input())
print("Enter final power of 2:")
finalPower = int(input())
print('%10s %10s %10s %10s %10s' % ("n","T(n)","lg n","n lg n","1/2n^2"))

for x in range(startPower, finalPower+1):
    n = 2**x
    Tn = T(n)
    test1 = math.log(n,2)
    test2 = n*math.log(n,2)
    test3 = 0.5*(n**2)
    print('%10d %10d %10d %10d %10d' % (n, Tn, test1, test2, test3))