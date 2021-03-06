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
        listOfCycles {[List]} -- [A list of lists indicating the cycles]
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
        self.listOfCycles = None
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

        self.startIndex = startIndex
        self.endIndex = endIndex
        self.backtrackingList = [0] * self.N

        # Crazy parts
        self.backtrackingList[0] = self.startIndex
        currentVertex = 1

        self.graph = graph
        self.listOfCycles = []
        self.hamiltonian(currentVertex)
        # self.finalHamiltonianPaths = self.findGoodPaths()
        # print(self.finalHamiltonianPaths)
        print(self.listOfCycles)
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
                    print("EHRE")
                    self.listOfCycles.append(self.backtrackingList[0:self.N])
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

            # print(self.backtrackingList)

            if (self.backtrackingList[currentVertex] == 0):
                return
            
            if (self.graph[ self.backtrackingList[currentVertex - 1] - 1 ][ self.backtrackingList[currentVertex] - 1 ] != 0):
                j = 0
                while j in range(0, currentVertex):
                    if (self.backtrackingList[j] == self.backtrackingList[currentVertex]):
                        break
                    j += 1

                if j == currentVertex and (currentVertex < self.N) or ( (currentVertex == self.N) and ( self.graph[ self.backtrackingList[self.N] - 1][ self.backtrackingList[0] - 1] != 0 ) ):
                    return
        return



graph = Graph.GraphObject(10,40,"UnDirected")
# print(graph.getListAdjacencyMatrix())
graph.showGraph()
graphList = graph.getListAdjacencyMatrix()

solver = SolveHamiltonian()

# graphList = [[0,1,1,0,1],
#             [1,0,1,1,1],
#             [1,1,0,1,0],
#             [0,1,1,0,1],
#             [1,1,0,1,0]]
# graphList[1][2] = 1
# graphList[2][1] = 1

# graphList = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 0], [1, 1, 1, 0, 0]]
# graphList = [[0, 1, 0, 1, 0],
#             [0, 0, 1, 1, 1],
#             [1, 1, 0, 1, 1],
#             [1, 1, 0, 0, 1],
#             [0, 1, 1, 1, 0]]
# for x in graphList:
#     print(x)
# input()

solver.findHamiltonianPaths(graphList, 1, 3)