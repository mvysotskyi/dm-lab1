"""
Kruskal and Prim algorithms.
"""

from graph_generator import gnp_random_connected_graph

def kruskal_search(graph) -> list:
    """
    Implements the Kruskal's algorithm to find
    the minimum spanning tree of a graph.
    Returns list[tuple], where tuple is tuple of nodes.
    >>> import networkx as nx
    >>> G = nx.Graph()
    >>> G.add_edge(1, 2, weight=2)
    >>> G.add_edge(1, 3, weight=3)
    >>> G.add_edge(2, 3, weight=1)
    >>> kruskal_search(G)
    [(1, 2), (2, 3)]
    """
    edges = sorted(graph.edges(data=True), key = lambda x: x[2]['weight']) 
    #list of sorted weights
    points = [{i} for i in list(graph.nodes())]
    result = []
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
            result.append((edge[0], edge[1]))   
    return sorted(result, key = lambda x: x[0])
