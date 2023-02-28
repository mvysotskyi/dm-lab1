"""
Prim's algorithm for finding the minimum spanning tree of a graph.
"""

import networkx as nx
from queue import PriorityQueue

def prim_mst(graph: nx.Graph) -> nx.Graph:
    """
    Implements the Prim's algorithm to find
    the minimum spanning tree of a graph.
    Returns list[tuple], where tuple is tuple of nodes.

    Parameters
    ----------
    graph : nx.Graph
        Graph to find the minimum spanning tree of.
    
    Returns
    -------
    nx.Graph : Minimum spanning tree of the graph.
    """
    graph = graph.to_directed()
    visited = [False] * graph.number_of_nodes()
    visited[0] = True

    mst = nx.Graph()
    edges = PriorityQueue()

    for adj, data in graph.adj[0].items():
        if not visited[adj]:
            edges.put((data["weight"], 0, adj))

    while not edges.empty():
        weight, tree_vertex, vertex = edges.get()
        if visited[vertex]:
            continue
        mst.add_edge(tree_vertex, vertex, weight=weight)
        visited[vertex] = True

        for adj, data in graph.adj[vertex].items():
            if not visited[adj]:
                edges.put((data["weight"], vertex, adj))

    return mst
