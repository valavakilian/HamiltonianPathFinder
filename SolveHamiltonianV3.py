import numpy as np
import GenerateGraphs
import Graph
import networkx as nx 
import matplotlib.pyplot as plt

class SolveHamiltonian:
    """[Hamiltonian Solver]
    
    Returns:
        [Custom type] -- [Hamiltonian solver]
    
    Properties:
        graph {[networkx.graph]} -- [networkx graph object]
        N {[int]} -- [number of nodes]
        backtrackingList {[list]} -- [a list of ints used for backtracking by the hamiltonian solver]
        startIndex {[int]} -- [start index for the graph path]
        endIndex {[int]} -- [end index for the graph path]
        listOfPaths {[List]} -- [A list of lists indicating the cycles]
        finalHamiltonianPaths {[list]} -- [A list of lists indicating the paths]
    """
    def __init__(self):
        """[SolveHamiltonian constructor]
        """
        self.graph = None
        self.N = 0
        self.backtrackingList = []
        self.startIndex = None
        self.endIndex = None
        self.listOfPaths = None
        self.finalHamiltonianPaths = None
        return

    def findHamiltonianPaths(self, graph, startIndex, endIndex):
        """[A solver for finding the hamiltonian paths between the start and end index]
        
        Arguments:
            graph {[networkx.graph]} -- [networkx graph object]
            startIndex {[int]} -- [start index for the graph path]
            endIndex {[int]} -- [end index for the graph path]
        """
        self.N = len(graph)

        if startIndex not in range(1,self.N + 1) or endIndex not in range(1,self.N + 1):
            print("Error: start or end indices are out of range.")
            return


        # Adding the new dynamic programming part
        self.memoDict = {}

        self.startIndex = startIndex
        self.endIndex = endIndex
        self.backtrackingList = [0] * self.N

        self.backtrackingList[0] = self.startIndex
        currentVertex = 1

        self.graph = graph
        self.listOfPaths = []
        self.hamiltonian(currentVertex)
        self.printPaths()

        return
    
    def hamiltonian(self, currentVertex):
        """[Hamiltonian solver that iterates through the vertices of the graph.
            The function increments k one at a time.
            This function is a recursive function (could be optimized to reduce overhead
            using memoization )]
        
        Arguments:
            currentVertex {[int]} -- [current Vertex which starts from zero]
        """
        while True:
            self.nextVertex(currentVertex)

            if self.backtrackingList[0] != self.startIndex:
                return

            if self.backtrackingList[currentVertex] == 0:
                return
            if currentVertex == self.N - 1:
                if self.backtrackingList[-1] == self.endIndex:
                    print(self.backtrackingList[0:self.N])
                    self.listOfPaths.append(self.backtrackingList[0:self.N])
            else:
                self.hamiltonian(currentVertex + 1)
    
    def nextVertex(self, currentVertex):
        """[The function gives the next vertex in the path to consider.]
        
        Arguments:
            currentVertex {[int]} -- [index value of the current vertex number considered in the path. 
            (1st in the apth, 2nd in the path, 3rd in the path ... ) ]
        """
        while True:
            self.backtrackingList[currentVertex] = (self.backtrackingList[currentVertex] + 1) % (self.N + 1)

            if (self.backtrackingList[currentVertex] == 0):
                # print("Our 0 point is at vertex : ", currentVertex)
                print("Backtracking list is : ", self.backtrackingList)
                # input()
                return
            
            if (self.graph[ self.backtrackingList[currentVertex - 1] - 1 ][ self.backtrackingList[currentVertex] - 1 ] != 0):
                j = 0
                while j in range(0, currentVertex):
                    if (self.backtrackingList[j] == self.backtrackingList[currentVertex]):
                        break
                    j += 1

                if j == currentVertex and (currentVertex < self.N) or ( (currentVertex == self.N) and ( self.graph[ self.backtrackingList[self.N] - 1][ self.backtrackingList[0] - 1] != 0 ) ):
                    # print("->", self.backtrackingList)
                    return

        # print("->", self.backtrackingList)
        return

    
    def hamiltonianDP(self, graphList):

        n = len(graphList)
        for index in range(0,n):
            graphList[index][index] = 1
        
        dp = []
        for i in range(0,n):
            row = []
            for j in range(0,2**n):
                row.append(False)  
            dp.append(row)
        
        for i in range(0, n):
            dp[i][2 ** i] = True

        for i in range(0, 2 ** n):
            for j in range(0, n):
                iBitform = bin(i)[2:].zfill(n)
                if iBitform[j]:
                    for k in range(0,n):
                        if j != k and iBitform[k] and graphList[k][j] == 1 and dp[k][i ^ 2 ** j] == True:
                            dp[j][i] = True
                            break
        
        for m in dp:
            print(m)

        for i in range(0, n):
            if dp[i][2 ** n - 1] == True:
                return True

        return False


    def hamiltonianDPV2(self, graphList):

        # graphList = [[0,1,1,0],
        #              [1,0,1,1],
        #              [1,1,0,1],
        #              [0,1,1,1]]

        n = len(graphList)
        for index in range(0,n):
            graphList[index][index] = 1
        
        dp = []
        for node_index in range(0,n):
            dp_for_node = []
            for i in range(0,n):
                row = []
                for j in range(0,2**n):
                    row.append(0)  
                dp_for_node.append(row)
            dp.append(dp_for_node)
        
        for i in range(0, n):
            dp[i][i][2 ** i] = 1


        for table in dp:
            for i in range(0, 2 ** n):
                for j in range(0, n):
                    iBitform = bin(i)[2:].zfill(n)
                    if iBitform[j]:
                        for k in range(0,n):
                            if j != k and iBitform[k] and graphList[k][j] == 1 and table[k][i ^ 2 ** j] == 1:
                                table[j][i] += table[k][i ^ 2 ** j]
                                break
        
        for table_index in range(0,len(dp)):
            table = dp[table_index]
            # print(" ->" + "Table " + str(table_index))
            for m in table:
                print(m)

        # for i in range(0, n):
        #     if dp[i][2 ** n - 1] == True:
        #         return True

        return False


    def printPaths(self):
        """[Prints the hamiltonian paths]
        """
        print("List of Hamiltonian Paths from index " + str(self.startIndex) + " to index " + str(self.endIndex) + " are:" )
        for path in self.listOfPaths:
            pathString = ""
            pathString += str(path[0])
            for index in range(1, len(path)):
                pathString += " -> " + str(path[index])
            print(pathString)
        return



