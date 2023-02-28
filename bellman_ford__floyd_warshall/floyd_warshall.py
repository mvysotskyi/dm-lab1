def checking_cycle(graph):
    """
    Checks whether an input graph contains a negative cycle.
    """
    cycles = list(nx.simple_cycles(graph))
    edges = list(graph.edges(data=True))

    cycle_0 = {}
    for edge in edges:
        if edge[0] != edge[1]:
            cycle_0[(edge[0], edge[1])] = edge[2]

    for cyc in cycles:
        total_count = 0
        i = 0
        while i < len(cyc)-1:
            elem1 = cyc[i]
            elem2 = cyc[i+1]
            total_count += cycle_0[(elem1, elem2)]['weight']
            i += 1
        if total_count < 0 and len(cyc) > 2:
            print('Negative cycle! The result might be wrong.')
            return True
    return False


def warshall_search(graph):
    """
    Floyd-Warshall algorithm, main function.
    """
#     if checking_cycle(graph):
#         return None
    edges = graph.edges(data = True)
    k = len(graph.nodes())
    matrix = [[inf for i in range(k)] for j in range(k)]
    for ind in range(k):
        matrix[ind][ind] = 0
    for elem in edges:
        matrix[elem[0]][elem[1]] = elem[2]['weight']
    k = len(graph.nodes())
    for k_counter in range(1, k):
        for i in range(k):
            for j in range(k):
                matrix[i][j] = min(matrix[i][j], matrix[i][k_counter]+matrix[k_counter][j])
    for i in range(k):
        info = {}
        for ind, elem in enumerate(matrix[i]):
            info[ind] = elem
        print(f'Distances with {i} source: {info}')
