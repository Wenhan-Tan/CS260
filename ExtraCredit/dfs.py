import sys

ifCycle = 0
def DFSVisit(parsedFile, u):
    Dict[u] = 'grey'
    for i in parsedFile:
        if i[0] == u:
            if Dict[i[1]] == 'white':
                DFSVisit(parsedFile, i[1])
            elif Dict[i[1]] == 'grey':
                global ifCycle
                ifCycle = 1
    Dict[u] = 'black'

def DFS(parsedFile, numVertex):
    global Dict 
    Dict = {}
    for i in range(0, numVertex):
        Dict[i] = 'white'
    
    for i in range(0, numVertex):
        if Dict[i] == 'white':
            DFSVisit(parsedFile, i)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No File Name")
    else:
        fileName = (sys.argv)[1]
        file = open(fileName, 'r')
        numVertex = int(file.readline())
        parsedFile = []
        for line in file:
            temp = []
            temp = line.split()
            temp = map(int, temp)
            temp = list(temp)
            parsedFile.append(temp)
        file.close()
        DFS(parsedFile, numVertex)
        if ifCycle == 0:
            print("False")
        else:
            print("True")