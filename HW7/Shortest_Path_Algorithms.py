def d(xx, fileName):
    x = xx
    inf = float("inf")
    file = open(fileName, 'r')
    firstLine = int(file.readline())
    unVisited = [x]
    Visited = []
    finalList = [inf] * firstLine
    finalList[x] = 0
    parsedFile = []
    temp1 = []
    temp2 = []
    
    for line in file:
        parsedFile.append(line)
    file.close()
        
    while unVisited != []:
        del temp1[:]
        del temp2[:]
        for line in parsedFile:
            if int(line[0]) == x:
                if int(line[2]) not in Visited:
                    temp1.append(int(line[2]))
                    if len(line) > 5:
                        temp2.append(int(line[4:6]))
                    else:
                        temp2.append(int(line[4]))
                    if int(line[2]) not in unVisited:
                        unVisited.append(int(line[2]))
        for i in range(0, len(temp2)):
            value = temp2[i] + finalList[x]
            idx = temp1[i]
            
            if value < finalList[idx]:
                finalList[idx] = value

        # print(x, temp1, temp2)
        Visited.append(x)
        unVisited.pop(unVisited.index(x))

        if len(temp2) > 0:
            value = temp1[temp2.index(min(temp2))]
            x = value
            # print(1,x)
        elif len(unVisited) > 0:
            x = unVisited[0]
            # print(2,x)
        else:
            # print(3,x)
            break
        
        if len(temp2) == 2:
            if temp2[0] == temp2[1]:
                x = min(temp1)
        # print(finalList)
        
    for i in range(0, len(finalList)):
        finalList[i] = float(finalList[i])    
    print(finalList)

def f(fileName):
    file = open(fileName, 'r')
    firstLine = int(file.readline())
    for i in range(0, firstLine):
        d(i, fileName)

if __name__ == "__main__":
    fileName = input("File containing graph:")
    print("")
    print("Possible Commands are: ")
    print("dijkstra x - Runs Dijkstra starting at node X. X must be an integer")
    print("floyd - Runs Floyd's algorithm")
    print("help - prints this menu")
    print("exit or ctrl-D - Exits the program")
    command = input("Enter command:")
    print("")
    
    while (command != "exit"):
        if (len(command) > 7):
            d(int(command[9]), fileName)
        elif (len(command) == 5):
            f(fileName)
        elif (command == "help"):
            print("Possible Commands are: ")
            print("dijkstra x - Runs Dijkstra starting at node X. X must be an integer")
            print("floyd - Runs Floyd's algorithm")
            print("help - prints this menu")
            print("exit or ctrl-D - Exits the program")
        command = input("Enter command:")
        print("")
        
    print("Bye")