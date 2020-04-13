import numpy as np
import GenerateGraphs
import Graph
import networkx as nx 
import matplotlib.pyplot as plt
import SolveHamiltonianV3

graph = Graph.GraphObject(100,600,"UnDirected")
# print(graph.getListAdjacencyMatrix())
graph.showGraph()
graphList = graph.getListAdjacencyMatrix()
solver = SolveHamiltonianV3.SolveHamiltonian()
# solver.findHamiltonianPaths(graphList, 1, 3) 
# print(len(solver.listOfPaths))
print(solver.hamiltonianDP(graphList))