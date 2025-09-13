def pagerank(graph, iterations=20, d=0.85):
    """Compute PageRank scores for graph represented as adjacency lists.

    Time: O(iterations * (V + E)), Space: O(V)
    """
    nodes = list(graph.keys())
    n = len(nodes)
    rank = {node: 1 / n for node in nodes}
    for _ in range(iterations):
        new_rank = {node: (1 - d) / n for node in nodes}
        for node, out in graph.items():
            if not out:
                continue
            share = rank[node] / len(out)
            for dest in out:
                new_rank[dest] += d * share
        rank = new_rank
    return rank
