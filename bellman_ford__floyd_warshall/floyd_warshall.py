def creating_table(graph):
    """
    Creates a matrix for an input graph.
    A start for Floyd-Warshall algorithm.
    """
    edges = graph.edges(data = True)
    k = len(graph.nodes())
    matrix = [[inf for i in range(k)] for j in range(k)]
    cycle_0 = {}
    for edge in edges:
        if edge[0] != edge[1]:
            cycle_0[(edge[0], edge[1])] = edge[2]
    for i in range(k):
        for j in range(k):
            if i == j:
                matrix[i][j] = 0
            elif (i, j) in list(cycle_0.keys()):
                matrix[i][j] = cycle_0[(i, j)]['weight']
    return matrix


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
    checking_cycle(graph)
    started = creating_table(graph)
    k = len(graph.nodes())
    for k_counter in range(1, k):
        for i in range(k):
            for j in range(k):
                started[i][j] = min(started[i][j], started[i][k_counter]+started[k_counter][j])
    res = ''
    for i in range(k):
        info = {}
        for ind, elem in enumerate(started[i]):
            info[ind] = elem
        res += f'Distances with {i} source: {info}\n'
    return res.strip()
