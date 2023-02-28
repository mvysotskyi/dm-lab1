"""
Floyd-Warshall algorithm.
"""

import networkx as nx

def have_negative_cycle(matrix: list[list[float]]) -> bool:
    """
    Function checks for negative cycle in matrix.
    """
    for idx, _ in enumerate(matrix):
        if matrix[idx][idx] < 0:
            return True

    return False

def floyd_warshall_algorithm(graph: nx.Graph) -> list[list[float]]:
    """
    Function implements Floyd-Warshall's algorithm.
    If there is a negative cycle in graph, function returns None.
    """
    graph = graph.to_directed()
    num_nodes = graph.number_of_nodes()
    edges = graph.edges(data="weight")

    matrix = [[float("inf") for _ in range(num_nodes)] for _ in range(num_nodes)]

    for idx in range(num_nodes):
        matrix[idx][idx] = 0

    for edge in edges:
        matrix[edge[0]][edge[1]] = edge[2]

    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

    if have_negative_cycle(matrix):
        return None

    return matrix
