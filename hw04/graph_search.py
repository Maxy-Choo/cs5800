# Bruce A. Maxwell
# Summer 2025 Algorithms
# Skeleton cod for DFS and BFS Search
#
import simple_graph as gs

# global variable for handling pre/post
step = 0

# Executes a DFS search on graph starting at node
def dfs_explore( graph, node, verbose = False ):

    # use the global step variable
    global step

    # set the visited field of node to True
    node.setVisited(True)
    # set the pre field of node to step
    node.setPre(step)
    # increment step
    step += 1
    # for each neighbor n of node
    for n in node.neighbors():
        # if n has not been visited
        if not n["node"].visited():
            # set the parent of n to node
            n["node"].setParent(node)
            # call dfs_explore with the graph, n, and verbose
            dfs_explore(graph, n["node"], verbose)

    # set the post value to step
    node.setPost(step)
    # increment step
    step += 1

    if verbose:
        # print information about the node before returning
        parentid = -1
        if node.parent() != None:
            parentid = node.parent().id()
        print("Node %d (pre, post): (%d, %d)  parent %d" % (node.id(), node.pre(), node.post(), parentid) )

    return


# Executes DFS over the whole graph
def dfs( graph, verbose=False ):
    global step

    # set step to 0
    step = 0

    # initialize each node in the graph (visited -> False; pre -> -1; post -> -1; parent -> None)
    for n in graph:
        n.setVisited(False)
        n.setPre(-1)
        n.setPost(-1)
    # for each node in the graph
    for n in graph:
        # if the node is not visited
        if not n.visited():
            # call dfs_explore with graph, node, and verbose
            dfs_explore(graph, n, True)


    return


# Executes a BFS search starting at the given node
def bfs_explore( graph, node, verbose=False ):
    global step

    # set the node as visited
    node.setVisited(True)
    # initialize a queue (list)
    Queue = []
    # append the node to the queue
    Queue.append(node)
    # while the queue is not empty
    while Queue:
        # take the first element p off the queue (pop(0))
        p = Queue.pop(0)
        # set the pre value of p and increment step
        p.setPre(step)
        step += 1
        # set parentid to -1
        parentid = -1
        # if the parent node is not None
        if p.parent():
            # set parentid to the parent node ID
            parentid = p.parent().id()

        if verbose:
            print("Node %d pre: %d parent %d" % (p.id(), p.pre(), parentid ) )

        # for each node in the neighbors list of p
        for n in p.neighbors():
            # if the node is not visited
            if not n["node"].visited():
                # set visited to true
                n["node"].setVisited(True)
                # set the parent to p
                n["node"].setParent(p)
                # append the node to the queue
                Queue.append(n["node"])


    return


# Executes a BFS search of the entire graph
def bfs( graph, verbose=False ):
    global step

    # initialize step to 0
    step = 0
    # initialize each node in the graph (visited -> False; pre -> -1; post -> -1; parent -> None)
    for n in graph:
        n.setVisited(False)
        n.setPre(-1)
        n.setPost(-1)
        n.setParent(None)
    # for each node in the graph
    for n in graph:
        # if the node is not visited
        if not n.visited():
            # call bfs_explore with graph, node, and verbose
            bfs_explore(graph, n, True)


# Test function for DFS and BFS search on a simple graph
def main():

    # build a graph
    graph = []

    graph.append( gs.Node(0, 100, 100) )
    graph.append( gs.Node(1, 200,  20) )
    graph.append( gs.Node(2, 750, 100) )
    graph.append( gs.Node(3, 550, 150) )
    graph.append( gs.Node(4, 400, 250) )
    graph.append( gs.Node(5, 850, 400) )
    graph.append( gs.Node(6, 200, 350) )
    graph.append( gs.Node(7, 550, 450) )
    graph.append( gs.Node(8, 350, 550) )
    graph.append( gs.Node(9, 120, 600) )

    graph[0].addUndirectedNeighbor( graph[1] )
    graph[0].addUndirectedNeighbor( graph[6] )
    graph[1].addUndirectedNeighbor( graph[2] )
    graph[1].addUndirectedNeighbor( graph[4] )
    graph[2].addUndirectedNeighbor( graph[3] )
    graph[2].addUndirectedNeighbor( graph[5] )
    graph[3].addUndirectedNeighbor( graph[4] )
    graph[3].addUndirectedNeighbor( graph[5] )
    graph[3].addUndirectedNeighbor( graph[7] )
    graph[4].addUndirectedNeighbor( graph[6] )
    graph[6].addUndirectedNeighbor( graph[7] )
    graph[6].addUndirectedNeighbor( graph[8] )
    graph[6].addUndirectedNeighbor( graph[9] )
    graph[7].addUndirectedNeighbor( graph[8] )
    graph[8].addUndirectedNeighbor( graph[9] )


    dfs( graph, verbose=True )

    bfs( graph, verbose=True )

    return


if __name__ == "__main__":
    main()

