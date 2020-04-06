import numpy as np
import networkx as nx 
import matplotlib.pyplot as plt
import igraph as ig

class GraphObject:
    """[Graph Object]

       [Custom Type] -- [Has both directed and undirected graphs
                        Creates graphs based on the erdos_renyi method]

       Properties:
            numberOfEdges {[int]} -- [number of nodes]
            numberOfNodes {[int]} -- [number of Edges]
            typeOfGraph {[String]} -- [string indicating the type of graph Directed/UnDirected]
            graph {[igraph.graph]} -- [igraph graph object]
            labels {[dict]} -- [{int:String} dictionary for the labels]
            listMatrix {[List]} -- [A 2D list of 0s and 1s for the adjacency matrix]
            numpyMatrix {[numpy.matrix]} -- [A 2D numpy matrix of 0s and 1s for the adjacency matrix]
        
    """

    def __init__(self, numOfNodes, numOfEdges, typeOfGraph):
        """[GraphObject constructor]
        
        Arguments:
            numOfNodes {[int]} -- [number of nodes]
            numOfEdges {[int]} -- [number of Edges]
            typeOfGraph {[str]} -- [string indicating the type of graph Directed/UnDirected]

        """

        self.numberOfEdges = numOfEdges
        self.numberOfNodes = numOfNodes
        self.typeOfGraph = typeOfGraph
        self.listMatrix = None
        self.numpyMatrix = None
        self.graph = None
        self.labels = None

        if self.typeOfGraph != "Directed" and self.typeOfGraph != "UnDirected":
            print("Error: enter the correct type of graph")
            return
        
        if self.numberOfEdges > self.numberOfNodes * ( self.numberOfNodes - 1 ) / 2  and self.typeOfGraph == "UnDirected":
            print("Too manu edges. The graph is now complete.")
            self.numberOfEdges = self.numberOfNodes * ( self.numberOfNodes - 1 ) / 2

        if self.numberOfEdges > self.numberOfNodes * ( self.numberOfNodes - 1 )  and self.typeOfGraph == "Directed":
            print("Too manu edges. The graph is now complete.")
            self.numberOfEdges = self.numberOfNodes * ( self.numberOfNodes - 1 )
        
        # Label is a dictionary
        self.labels = np.asarray([label for label in range(1,self.numberOfNodes + 1)])
        self.labels = {(label - 1):str(label) for label in self.labels}

        # For two different cases
        if self.typeOfGraph == "UnDirected":
            self.graph = ig.Graph.Erdos_Renyi(n=self.numberOfNodes, m=self.numberOfEdges, directed=False)
            self.listMatrix = list(self.graph.get_adjacency())
            self.numpyMatrix = np.matrix(self.listMatrix)
        elif self.typeOfGraph == "Directed":
            self.graph = ig.Graph.Erdos_Renyi(n=self.numberOfNodes, m=self.numberOfEdges, directed=True)
            self.listMatrix = list(self.graph.get_adjacency())
            self.numpyMatrix = np.matrix(self.listMatrix)
        
        return
        
    
    def getListAdjacencyMatrix(self):
        """[Returns the adjacency matrix as a list]
        
        Returns:
            [list] -- [2D list adjacency matrix]
        """
        return self.listMatrix
    
    def getNumpyAdjacencyMatrix(self):
        """[Returns the adjacency matrix as a numpy matrix]
        
        Returns:
            [numpy.matrix] -- [2D numpy adjacency matrix]
        """
        return self.numpyMatrix
    
    def showGraph(self, saveFig = True):
        """[Shows the graph using networkx]
        
        Keyword Arguments:
            saveFig {bool} -- [saves the graph] (default: {True})
        """
        
        if self.graph is None:
            print("Error: No graph is currently generated. Returning.")
        elif self.typeOfGraph == "UnDirected":
            gr = nx.from_numpy_matrix(self.numpyMatrix)
            nx.draw(gr, node_size=500, labels=self.labels, with_labels=True, directed=True)
            plt.savefig('graph.png')
            plt.show()
        elif self.typeOfGraph == "Directed":
            G = nx.from_numpy_matrix(self.numpyMatrix, create_using=nx.MultiDiGraph())
            pos = nx.circular_layout(G)
            nx.draw_circular(G)
            labels = {i : i + 1 for i in G.nodes()}
            nx.draw_networkx_labels(G, pos, labels, font_size=15)
            plt.savefig('graph.png')
            plt.show()
        else:
            print("Error: Incorrect type of graph.")
        return
