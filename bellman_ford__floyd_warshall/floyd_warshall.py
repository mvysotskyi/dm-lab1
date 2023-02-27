"""
Floyd-Warshall algorithm for finding the shortest path between all pairs of nodes in a graph.
"""

def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm for finding the shortest path between all pairs of nodes in a graph.
    """
    n = graph.number_of_nodes()
    key_dict = {key: float("inf") for key in range(n)}
    matrix = {key: key_dict.copy() for key in range(n)}

    for n in graph.nodes():
        matrix[n][n] = 0

    for edge in graph.edges(data=True):
        matrix[edge[0]][edge[1]] = edge[2]['weight']

    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    return matrix
