"""
Bellman-Ford's alorithm implementation.
"""

import networkx as nx

def belman_ford_algorithm(graph: nx.Graph, start: int = 0) -> tuple[list[float], bool]:
    """
    Function implements Belman-Ford's algorithm.
    """
    graph = graph.to_directed()
    num_nodes = graph.number_of_nodes()
    edges = graph.edges(data="weight")

    distances = {idx: float("inf") for idx in range(num_nodes)}
    distances[start] = 0

    for _ in range(num_nodes - 1):
        for edge in edges:
            if distances[edge[1]] > (distances[edge[0]] + edge[2]):
                distances[edge[1]] = distances[edge[0]] + edge[2]

    for edge in edges:
        if distances[edge[1]] > ( distances[edge[0]] + edge[2]):
            return False

    return distances, True
