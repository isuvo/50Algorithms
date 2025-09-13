"""
Bellman-Ford shortest path algorithm.

This implementation relaxes all edges |V|-1 times, allowing detection of
shortest paths even with negative edge weights.

Time Complexity: O(V * E)
Space Complexity: O(V)
"""
from typing import Dict, List, Tuple, Hashable


def bellman_ford(graph: Dict[Hashable, List[Tuple[Hashable, float]]], start: Hashable) -> Dict[Hashable, float]:
    """Return the shortest distance from *start* to every other node.

    Raises
    ------
    ValueError
        If a negative-weight cycle is detected.
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
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
                    updated = True
        if not updated:
            break

    # Check for negative cycles
    for u in nodes:
        for v, w in graph.get(u, []):
            if distances[u] + w < distances[v]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distances
