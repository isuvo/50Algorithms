"""
Floyd-Warshall all-pairs shortest path algorithm.

Uses dynamic programming to iteratively improve the shortest distance between
all pairs of vertices by considering each vertex as an intermediate point.

Time Complexity: O(V^3)
Space Complexity: O(V^2)
"""
from typing import Dict, Hashable


def floyd_warshall(graph: Dict[Hashable, Dict[Hashable, float]]) -> Dict[Hashable, Dict[Hashable, float]]:
    """Return a distance matrix mapping node pairs to their shortest distance."""
    nodes = list(graph.keys())
    dist: Dict[Hashable, Dict[Hashable, float]] = {
        u: {v: float("inf") for v in nodes} for u in nodes
    }
    for u in nodes:
        dist[u][u] = 0.0
        for v, w in graph.get(u, {}).items():
            dist[u][v] = w

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
