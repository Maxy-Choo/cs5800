from simple_graph import Node
import graph_search as gs
import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(graph):
    G = nx.Graph()

    pos = {}
    edges = []
    for n in graph:
        pos[n.id()] = (n.x(), n.y())
        for nei in n.neighbors():
            edges.append((n.id(), nei["node"].id()))
    
    G.add_nodes_from(pos.keys())
    G.add_edges_from(edges)

    plt.figure(figsize=(10, 8))
    nx.draw_networkx_edges(G, pos, width=2.5, edge_color="black")
    nx.draw_networkx_nodes(G, pos, node_size=150, node_color="black")

    for node_id, (x, y) in pos.items():
        plt.text(
            x+15,
            y+15,
            f"{node_id}: ({x}, {y})",
            fontsize=11,
            color="#555555",
            ha="left",
            va="center"
        )
    
    plt.axis("off")
    plt.tight_layout()
    plt.show()


def main():
    graph = []
    graph.append(Node(0, 200, 0))
    graph.append(Node(1, 0, 200))
    graph.append(Node(2, 400, 200))
    graph.append(Node(3, 0, 400))
    graph.append(Node(4, 400, 400))
    graph.append(Node(5, 200, 600))
    graph.append(Node(6, 600, 600))
    graph.append(Node(7, 400, 800))
    graph.append(Node(8, 800, 800))
    graph.append(Node(9, 400, 1000))
    graph.append(Node(10, 800, 1000))
    graph.append(Node(11, 600, 1200))

    graph[0].addUndirectedNeighbor( graph[1] )
    graph[0].addUndirectedNeighbor( graph[2] )
    graph[1].addUndirectedNeighbor( graph[2] )
    graph[1].addUndirectedNeighbor( graph[3] )
    graph[2].addUndirectedNeighbor( graph[4] )
    graph[3].addUndirectedNeighbor( graph[4] )
    graph[5].addUndirectedNeighbor( graph[3] )
    graph[5].addUndirectedNeighbor( graph[4] )

    graph[6].addUndirectedNeighbor( graph[7] )
    graph[6].addUndirectedNeighbor( graph[8] )
    graph[7].addUndirectedNeighbor( graph[9] )
    graph[7].addUndirectedNeighbor( graph[10] )
    graph[8].addUndirectedNeighbor( graph[9] )
    graph[8].addUndirectedNeighbor( graph[10] )
    graph[11].addUndirectedNeighbor( graph[9] )
    graph[11].addUndirectedNeighbor( graph[10] )

    gs.bfs(graph, verbose=True)
    gs.dfs(graph, verbose=True)

    draw_graph(graph)

    return

if __name__ == "__main__":
    main()