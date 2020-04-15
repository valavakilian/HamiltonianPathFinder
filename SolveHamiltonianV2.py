import numpy as np
import Graph
import networkx as nx 
import matplotlib.pyplot as plt
import time

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
        self.listOfPaths = []
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

        self.startIndex = startIndex
        self.endIndex = endIndex
        self.backtrackingList = [0] * self.N

        self.backtrackingList[0] = self.startIndex
        currentVertex = 1

        self.graph = graph
        self.listOfPaths = []
        self.hamiltonian(currentVertex)

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
                    # Uncomment to see backtracking
                    # print(self.backtrackingList[0:self.N])
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
                # To see the backtracking, uncomment these parts
                # print("Our 0 point is at vertex : ", currentVertex)
                # print("Backtracking list is : ", self.backtrackingList)
                return
            
            if (self.graph[ self.backtrackingList[currentVertex - 1] - 1 ][ self.backtrackingList[currentVertex] - 1 ] != 0):
                j = 0
                while j in range(0, currentVertex):
                    if (self.backtrackingList[j] == self.backtrackingList[currentVertex]):
                        break
                    j += 1

                if j == currentVertex and (currentVertex < self.N) or ( (currentVertex == self.N) and ( self.graph[ self.backtrackingList[self.N] - 1][ self.backtrackingList[0] - 1] != 0 ) ):
                    # To see the backtracking, uncomment these parts
                    # print("->", self.backtrackingList)
                    return

        # To see the backtracking, uncomment these parts
        # print("->", self.backtrackingList)
        return
    
    def printPaths(self):
        """[Prints the hamiltonian paths]
        """
        print("Total number of existing hamiltonian paths are : ")
        print(len(self.listOfPaths))
        time.sleep(3)
        print("List of Hamiltonian Paths from index " + str(self.startIndex) + " to index " + str(self.endIndex) + " are:" )
        for path in self.listOfPaths:
            pathString = ""
            pathString += str(path[0])
            for index in range(1, len(path)):
                pathString += " -> " + str(path[index])
            print(pathString)
        return



