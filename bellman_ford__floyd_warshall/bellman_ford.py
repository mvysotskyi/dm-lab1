"""
Bellman-Ford's alorithm implementation.
"""

def belman_ford_algorithm(graph, start):
    """
    Function implements Belman-Ford's algorithm.
    """
    n = len(graph.nodes())
    edges = graph.edges()

    distances = {i: 0xFFFFFF for i in range(1, n + 1)}
    distances[start] = 0

    for _ in range(n - 1):
        for edge in edges:
            if distances[edge[1]] > (distances[edge[0]] + edge[2]):
                distances[edge[1]] = distances[edge[0]] + edge[2]

    for edge in edges:
        if distances[edge[1]] > ( distances[edge[0]] + edge[2]):
            return False

    return distances, True
