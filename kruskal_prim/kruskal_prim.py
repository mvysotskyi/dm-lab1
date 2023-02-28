"""
Kruskal and Prim algorithms.
"""

import networkx as nx
from queue import PriorityQueue

def kruskal_search(graph: nx.Graph) -> nx.Graph:
    """
    Implements the Kruskal's algorithm to find
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
    edges = sorted(graph.edges(data=True), key = lambda x: x[2]['weight'])
    #list of sorted weights
    points = [{i} for i in list(graph.nodes())]
    result = nx.Graph()
    ind1, ind2 = None, None
    for edge in edges:
        for point in points:
            if edge[0] in point:
                ind1 = points.index(point)
            if edge[1] in point:
                ind2 = points.index(point)
        if ind1 != ind2:
            points[ind1] = points[ind1].union(points[ind2])
            del points[ind2]
            # result.append((edge[0], edge[1])) 
            result.add_edge(edge[0], edge[1], weight=edge[2]['weight'])  
    # return sorted(result, key = lambda x: x[0])
    return result

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
