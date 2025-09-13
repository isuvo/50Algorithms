"""
Floyd-Warshall all-pairs shortest path algorithm.

Uses dynamic programming to iteratively improve the shortest distance between
all pairs of vertices by considering each vertex as an intermediate point.

Time Complexity: O(V^3), where V is the number of vertices.
Space Complexity: O(V^2), where V is the number of vertices.
"""
from typing import Dict, Hashable, List

Graph = Dict[Hashable, Dict[Hashable, float]]

def floyd_warshall(graph: Graph) -> Dict[Hashable, Dict[Hashable, float]]:
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
                if dist[i][k] != float('inf') and dist[k][j] != float('inf') and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

if __name__ == "__main__":
    graph = {
        0: {1: 3, 2: 8, 4: -4},
        1: {3: 1, 4: 7},
        2: {1: 4},
        3: {0: 2, 2: -5},
        4: {3: 6}
    }
    distances = floyd_warshall(graph)
    print("Shortest distances between all pairs of vertices:")
    for i in sorted(distances.keys()):
        for j in sorted(distances[i].keys()):
            print(f"From {i} to {j}: {distances[i][j]}")