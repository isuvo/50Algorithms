"""
Bellman-Ford shortest path algorithm.

This implementation of the Bellman-Ford algorithm finds the shortest paths from
a single source vertex to all of the other vertices in a weighted digraph. It
can also detect negative weight cycles.

Time Complexity: O(V * E), where V is the number of vertices and E is the
number of edges.
Space Complexity: O(V), where V is the number of vertices.
"""
from typing import Dict, List, Tuple, Hashable

Graph = Dict[Hashable, List[Tuple[Hashable, float]]]

def bellman_ford(graph: Graph, start: Hashable) -> Dict[Hashable, float]:
    """
    Return the shortest distance from *start* to every other node.

    Args:
        graph: The graph represented as a dictionary of adjacency lists.
        start: The starting node.

    Returns:
        A dictionary mapping each node to its shortest distance from the start
        node.

    Raises:
        ValueError: If a negative-weight cycle is detected.
    """
    # Initialize distances
    distances: Dict[Hashable, float] = {node: float("inf") for node in graph}
    distances[start] = 0.0

    # Relax edges repeatedly
    nodes = list(graph.keys())
    for _ in range(len(nodes) - 1):
        updated = False
        for u in nodes:
            for v, w in graph.get(u, []):
                if distances[u] != float("inf") and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
                    updated = True
        if not updated:
            break

    # Check for negative cycles
    for u in nodes:
        for v, w in graph.get(u, []):
            if distances[u] != float("inf") and distances[u] + w < distances[v]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distances

if __name__ == "__main__":
    graph = {
        'A': [('B', -1), ('C', 4)],
        'B': [('C', 3), ('D', 2), ('E', 2)],
        'C': [],
        'D': [('B', 1), ('C', 5)],
        'E': [('D', -3)]
    }
    start_node = 'A'
    try:
        distances = bellman_ford(graph, start_node)
        print(f"Shortest distances from {start_node}:")
        for node, distance in sorted(distances.items()):
            print(f"- {node}: {distance}")
    except ValueError as e:
        print(e)