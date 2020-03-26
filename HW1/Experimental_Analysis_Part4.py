#Mark Boady
#CS260 - Homework 1 Linear Search Template

def LinearSearch(needle,haystack):
    for x in range(len(haystack)):
        print("Comparing element", haystack[x], "to needle", needle)
        
        if needle == haystack[x]:
            return True
        elif needle < haystack[x]:
            return False
    
    return False

#Do not make changes below this line.
import random
print("Welcome to Linear Search Test")
x=input("Enter Seed to Test:\n")
random.seed(x)
target=random.randint(0,20)
list=[random.randint(0,20) for x in range(0,10)]
list.sort()
print("Looking for", target)
print("In list", list)
x = LinearSearch(target,list)
if x==True:
    print("Target was found.")
else:
    print("Target was not found.")
