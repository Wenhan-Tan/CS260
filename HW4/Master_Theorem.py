import math

if __name__ == "__main__":
    print("Automated Master Theorem")
    print("Enter Formula T(n)=a*T(n/b)+n^x*(log2(n)^y)")
    a = int(input("Enter a value:\n"))
    b = int(input("Enter b value:\n"))
    x = int(input("Enter x value:\n"))
    y = int(input("Enter y value:\n"))
    c = int(math.log(a,b))
    if c == x:
        print("T(n)=Theta(" + "n^" + str(c) + " log2(n)^" + str(y+1) + ")")
    elif c < x:
        print("T(n)=Theta(n^" + str(x) + ")")
    else:
        print("T(n)=Theta(n^" + str(c) + ")")