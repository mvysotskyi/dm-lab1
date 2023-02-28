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

def timing(values):
    random_fullfil = [random.random() for i in range(49)]
    iterations = 1000
    time_taken = 0
    nx_time_taken = 0
    list_time_taken = []
    nx_list_time_taken = []
    for i in range(len(values)):
        print(i)
        graph = gnp_random_connected_graph(values[i], random_fullfil[i], False, False)
        for j in range(iterations):
            start = time.time()
            tree.minimum_spanning_tree(graph, algorithm="kruskal")
            end = time.time()
            nx_time_taken += end - start
            start = time.time()
            kruskal_search(graph)
            end = time.time()
            time_taken += end - start
        list_time_taken.append(time_taken/iterations)
        nx_list_time_taken.append(nx_time_taken/iterations)
    return list_time_taken, nx_list_time_taken


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
    values = range(10, 500, 10)
    kruskal_times, nx_times = timing(values)
    print(f'Minimal value of written algorithm: {min(kruskal_times)}, \
            Maximum value: {max(kruskal_times)}')
    print(f'Minimal value of implemented algorithm: {min(nx_times)}, \
            Maximum value: {max(nx_times)}')
    plt.plot(values, kruskal_times, label="Written")
    plt.plot(values, nx_times, label="Nx")
    plt.legend()
    plt.xlabel("Graph size")
    plt.ylabel("Time (seconds)")
    plt.show()

