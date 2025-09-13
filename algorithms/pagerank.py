"""
PageRank algorithm for ranking nodes in a graph.

This implementation of the PageRank algorithm ranks the nodes in a graph based
on their importance. It is a probabilistic algorithm that simulates a random
walker on the graph and assigns a rank to each node based on the frequency of
visits.

Time Complexity: O(i * (V + E)), where i is the number of iterations, V is the
number of vertices, and E is the number of edges.
Space Complexity: O(V), where V is the number of vertices.
"""
from typing import Dict, List, Hashable

Graph = Dict[Hashable, List[Hashable]]

def pagerank(graph: Graph, iterations: int = 20, d: float = 0.85) -> Dict[Hashable, float]:
    """
    Compute PageRank scores for a graph represented as adjacency lists.

    Args:
        graph: The graph represented as a dictionary of adjacency lists.
        iterations: The number of iterations to run the algorithm.
        d: The damping factor.

    Returns:
        A dictionary mapping each node to its PageRank score.
    """
    nodes = list(graph.keys())
    n = len(nodes)
    rank = {node: 1 / n for node in nodes}
    for _ in range(iterations):
        new_rank = {node: (1 - d) / n for node in nodes}
        for node, out in graph.items():
            if not out:
                # In the original paper, pages with no outgoing links are
                # assumed to link to all other pages in the collection.
                # Here we distribute the rank of such pages evenly among all pages.
                share = rank[node] / n
                for dest in nodes:
                    new_rank[dest] += d * share
            else:
                share = rank[node] / len(out)
                for dest in out:
                    new_rank[dest] += d * share
        rank = new_rank
    return rank

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['C'],
        'C': ['A'],
        'D': ['C']
    }
    ranks = pagerank(graph)
    print("PageRank scores:")
    for node, rank in sorted(ranks.items(), key=lambda item: item[1], reverse=True):
        print(f"- {node}: {rank:.4f}")