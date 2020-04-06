import numpy as np
import GenerateGraphs
import Graph
import networkx as nx 
import matplotlib.pyplot as plt
import SolveHamiltonianV2

graph = Graph.GraphObject(10,32,"UnDirected")
# print(graph.getListAdjacencyMatrix())
graph.showGraph()
graphList = graph.getListAdjacencyMatrix()
solver = SolveHamiltonianV2.SolveHamiltonian()
solver.findHamiltonianPaths(graphList, 1, 3)
print(len(solver.listOfPaths))