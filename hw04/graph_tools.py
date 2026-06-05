# Bruce A. Maxwell
# Summer 2025
# CS 5800 Algorithms
# Library of tools for working with graphs

import sys
import random
import simple_graph as gs
import matplotlib.pyplot as plt
import graph_search as g


# builds a random undirected graph with the given number of vertices [0, 1000] and average degree [0, nVertex-1].
# The function returns a list of Node objects, one per vertex
def buildRandomUndirectedGraph( nVertex, degree ):

    # build the nodes
    graph = [gs.Node(i) for i in range(nVertex)]

    degree = min( degree, nVertex-1 )
    nEdges = int(degree * nVertex // 2) # divide by 2 b/c degree = 2E / V

    nEdges = min( nEdges, nVertex*(nVertex-1)//2 )
    print("nEdges", nEdges, "degree", degree)

    # create a list of all possible edges
    edges = []
    for i in range(nVertex):
        for j in range(i+1, nVertex):
            edges.append( (i, j) )

    # shuffle all possible edges
    random.shuffle(edges)
    print("len(edges)", len(edges))

    # add the proper number of edges to the graph
    for i in range(nEdges):
        graph[ edges[i][0] ].addUndirectedNeighbor( graph[edges[i][1]] )
    
    return graph

def count_fully_connected(graph):
    ans = 0
    for node in graph:
        g.dfs_explore(graph, node, False)
        flag = 0
        for node in graph:
            if not node.visited():
                flag = 1
            node.setVisited(False)
        if not flag:
            ans += 1
    return ans

def analyse():
    N_set = [20, 100, 500]
    f_set = []
    for f in range(1, 25):
        f_set.append(f*0.5)

    for N in N_set:
        fully_connected_node_num = []
        for f in f_set:
            temp = 0
            for _ in range(20):
                graph = buildRandomUndirectedGraph( N, f )
                temp += count_fully_connected(graph)
            fully_connected_node_num.append(temp//20)
    
        plt.plot(f_set, fully_connected_node_num)
        plt.xlabel("Average degrees")
        plt.ylabel("Nums of fully-connected nodes")
        plt.title(f"Probability of Fully-Connected Nodes when N={N}")
        plt.show()

def main(args):

    N = 10
    f = 0.3
    
    if len(args) > 1:
        N = int(args[1])

    if len(args) > 2:
        f = float(args[2])

    print("Creating graph with %d vertices and %.2f density" % (N, f) )

    graph = buildRandomUndirectedGraph( N, f )

    #print the nodes in the graph and each adjacency list
    print("Graph:")
    for node in graph:
        s = "["
        for n in node.neighbors():
            s += str(n["node"]) + ", "
        s += "]"
        print(node, s)

    return

if __name__ == "__main__":
    main(sys.argv)
    analyse()


