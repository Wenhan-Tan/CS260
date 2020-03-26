def T(n):
    print("Analysis of Double Nested Loop")
    print("Enter starting power of 2:")
    startPower = int(input())
    print("Enter final power of 2:")
    finalPower = int(input())
    
    print('%10s %10s %10s %10s %10s' % ("n","T(n)","1/2n^2","n^2","2n^2"))
    
    for x in range(startPower, finalPower+1):
        n = 2**x;
        Tn = (n*(n-1)/2) + n
        test1 = 0.5*(n**2)
        test2 = (n**2)
        test3 = 2*(n**2)
        print('%10d %10d %10d %10d %10d' % (n, Tn, test1, test2, test3))

T(2)