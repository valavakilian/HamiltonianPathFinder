from numpy import genfromtxt
import numpy as np
mydata = genfromtxt('somethin.csv', delimiter=',')
print(mydata)
print(type(mydata))


adjacency = mydata[1:,1:]
print(adjacency)


import matplotlib.pyplot as plt
import networkx as nx

def show_graph_with_labels(adjacency_matrix, mylabels):
    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)
    nx.draw(gr, node_size=500, labels=mylabels, with_labels=True)
    plt.show()

# labList= [int(v) for k,v in qs[0].items()]
show_graph_with_labels(adjacency, {0:"a", 1:"b", 2:"c", 3:"d"})




def createEmptyMemoTable(N):
    memo = np.full((N,2 ** N), False, dtype=bool)
    memo = memo.tolist()
    for i in range(0,N):
        memo[i][2**i] = True
    return memo




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