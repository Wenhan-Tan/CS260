import math

def T(n):
    if n == 1:
        return 1
    
    Tn = 2 * T(n/2) + n
    
    return Tn

print("Analysis of First Recursive Function")
print("Enter starting power of 2:")
startPower = int(input())
print("Enter final power of 2:")
finalPower = int(input())
print('%10s %10s %10s %10s %10s' % ("n","T(n)","n lg n","1/2n^2","n^2"))

for x in range(startPower, finalPower+1):
    n = 2**x
    Tn = T(n)
    test1 = n*math.log(n,2)
    test2 = 0.5*(n**2)
    test3 = n**2
    print('%10d %10d %10d %10d %10d' % (n, Tn, test1, test2, test3))