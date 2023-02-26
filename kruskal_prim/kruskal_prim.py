"""
Kruskal and Prim algorithms.
"""

from graph_generator import gnp_random_connected_graph

def kruskal_search(graph):
    edges = sorted(graph.edges(data=True), key = lambda x: x[2]['weight'])
    #list of sorted weights
    points = [{i} for i in list(graph.nodes())]
    result = []
    ind1 = None
    ind2 = None
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
    return result
