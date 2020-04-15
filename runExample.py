import numpy as np
import Graph
import networkx as nx 
import matplotlib.pyplot as plt
import SolveHamiltonianV2

new_graph = "y"
new_start_end = "y"
continue_commands = "y"


while continue_commands == "y":

    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")


    if new_graph == "y":
        n = int(input("Enter number of nodes please : "))
        e = int(input("Enter number of edges please : "))
        graph_type = int(input("Enter the type of graph (0: directed), (1>=: undirected) :"))
        graph_type = "Directed" if graph_type == 0 else "UnDirected"  
        graph = Graph.GraphObject(n,e,graph_type)
        graph.showGraph()
        graphList = graph.getListAdjacencyMatrix()
        solver = SolveHamiltonianV2.SolveHamiltonian()


    if new_start_end == "y":    
        start = int(input("Please enter index for start node: "))
        end = int(input("Please enter index for end node: "))
        solver.findHamiltonianPaths(graphList, start, end) 
    

    print_paths = input("Would you like to print ? (enter y for yes, anything else for no):")
    if print_paths == "y":
        solver.printPaths()
    
    continue_commands = input("Would you like to continue ? (enter y for yes, anything else for no): ")
    if continue_commands == "y":    
        new_graph = input("Would you like to make a new graph ? (enter y for yes, anything else for no): ")
        new_start_end = input("Would you like to have a new start or end? (enter y for yes, anything else for no): ")

print("Thank you. ")