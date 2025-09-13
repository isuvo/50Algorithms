"""
Dijkstra's shortest path algorithm.

This algorithm computes the shortest paths from a starting node to all other
nodes in a weighted graph with non-negative edge weights.

Time Complexity: O(E log V) using a priority queue, where V is the number of
vertices and E is the number of edges.
Space Complexity: O(V), where V is the number of vertices.
"""
import heapq
from typing import Dict, List, Tuple, Hashable

Graph = Dict[Hashable, List[Tuple[Hashable, float]]]

def dijkstra(graph: Graph, start: Hashable) -> Dict[Hashable, float]:
    """Return a mapping of nodes to their minimum distance from *start*."""
    distances: Dict[Hashable, float] = {node: float('inf') for node in graph}
    distances[start] = 0.0
    heap: List[Tuple[float, Hashable]] = [(0.0, start)]
    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distances.get(node, float('inf')):
            continue
        for neighbor, weight in graph.get(node, []):
            new_dist = dist + weight
            if new_dist < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return distances

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    start_node = 'A'
    distances = dijkstra(graph, start_node)
    print(f"Shortest distances from {start_node}:")
    for node, distance in sorted(distances.items()):
        print(f"- {node}: {distance}")