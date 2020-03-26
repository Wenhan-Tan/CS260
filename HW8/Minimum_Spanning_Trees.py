def printCommand():
    print("Commands: ")
    print("exit or ctrl-d - quits the program")
    print("help - prints this menu")
    print("prim integer_value - run's Prim's algorithm starting at node given")
    print("kruskal - runs Kruskal's algorithm")

def kruskal(parsedFile, numVertex):
    parsedFile = sorted(parsedFile, key=lambda i:i[2])
    listEdge = []
    # testCount = 0
    
    for edge in parsedFile:
        ifCycle = 0
        for i in listEdge:
            if (edge[0] in i) and (edge[1] in i):
                ifCycle = ifCycle + 1
        
        ifExist1 = 0
        ifExist2 = 0
        if ifCycle == 0:
            if edge[0] > edge[1]:
                result = [edge[1], edge[0], edge[2]]
            else:
                result = edge
            result[2] = float(result[2])
            print("Select Edge:", result)
            if listEdge == []:
                listEdge.append([edge[0], edge[1]])
            else:
                for i in listEdge:
                    if edge[0] in i:
                        idx1 = listEdge.index(i)
                        ifExist1 = 1
                    if edge[1] in i:
                        idx2 = listEdge.index(i)
                        ifExist2 = 1
                if ifExist1 == 1 and ifExist2 == 1:
                    # print("idx1:", idx1)
                    # print("idx2:", idx2)
                    temp = listEdge[idx1] + listEdge[idx2]
                    if idx1 > idx2:
                        listEdge.pop(idx1)
                        listEdge.pop(idx2)
                    elif idx1 < idx2:
                        listEdge.pop(idx2)
                        listEdge.pop(idx1)
                    listEdge.append(temp)
                elif ifExist1 == 1:
                    listEdge[idx1].append(edge[1])
                elif ifExist2 == 1:
                    listEdge[idx2].append(edge[0])
                else:
                    listEdge.append([edge[0], edge[1]])
        # print("listEdge:", listEdge)
        # testCount = testCount + 1
        # if testCount == 7:
        #     break
    
    return

def prim(parsedFile, start):
    print("Starting Node:", start)
    listEdge = []
    visitedVertex = [start]
    current = start
    ifParse = 1
    
    while(1):
        temp = []
        if ifParse == 1:
            for i in parsedFile:
                if i[0] == current or i[1] == current:
                    listEdge.append(i)
                    temp.append(i)
            for i in temp:    
                parsedFile.pop(parsedFile.index(i))
            listEdge = sorted(listEdge, key=lambda i:i[2])
            
        if (listEdge[0][0] in visitedVertex) and (listEdge[0][1] in visitedVertex):
            listEdge.pop(0)
            ifParse = 0
            if listEdge == []:
                break
            else:
                if listEdge[0][0] in visitedVertex and listEdge[0][1] not in visitedVertex:
                    current = listEdge[0][1]
                elif listEdge[0][1] in visitedVertex and listEdge[0][0] not in visitedVertex:
                    current = listEdge[0][0]
        else:
            if listEdge[0][0] > listEdge[0][1]:
                result = [listEdge[0][1], listEdge[0][0], listEdge[0][2]]
            else:
                result = listEdge[0]
            
            if listEdge[0][0] in visitedVertex and listEdge[0][1] not in visitedVertex:
                current = listEdge[0][1]
                print("Added", listEdge[0][1])
            elif listEdge[0][1] in visitedVertex and listEdge[0][0] not in visitedVertex:
                current = listEdge[0][0]
                print("Added", listEdge[0][0])
            ifParse = 1
            
            result[2] = float(result[2])
            print("Using Edge", result)
                
            if listEdge[0][0] not in visitedVertex:
                visitedVertex.append(listEdge[0][0])
            elif listEdge[0][1] not in visitedVertex:
                visitedVertex.append(listEdge[0][1])
            listEdge.pop(0)
            if listEdge == []:
                break

if __name__ == '__main__':
    print("Welcome to Minimum Spanning Tree Finder")
    fileName =input("Give the file name graph is in:")
    print("")
    printCommand()
    command = ""

    while (1):
        command = input("Enter command:")
        print("")
        if command == "help":
            printCommand()
        elif command == "exit":
            print("Bye")
            break
        elif command == "kruskal":
            print("Running Kruskal's Algorithm")
            
            file = open(fileName, 'r')
            numVertex = int(file.readline())
            parsedFile = []
            for line in file:
                temp = []
                if len(temp) > 5:
                    temp = [int(line[0]), int(line[2]), int(line[4:5])]
                else:
                    temp = [int(line[0]), int(line[2]), int(line[4:6])]
                parsedFile.append(temp)
            file.close()
            
            kruskal(parsedFile, numVertex)
        elif command[0:4] == "prim":
            print("Running Prim's Algorithm")
            
            file = open(fileName, 'r')
            numVertex = int(file.readline())
            parsedFile = []
            for line in file:
                temp = []
                if len(temp) > 5:
                    temp = [int(line[0]), int(line[2]), int(line[4:5])]
                else:
                    temp = [int(line[0]), int(line[2]), int(line[4:6])]
                parsedFile.append(temp)
            file.close()
            
            prim(parsedFile, int(command[5]))
        else:
            print("Unknown Command")