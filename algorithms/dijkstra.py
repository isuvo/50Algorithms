"""
Dijkstra's shortest path algorithm.

This algorithm computes the shortest paths from a starting node to all other
nodes in a weighted graph with non-negative edge weights.

Time Complexity: O(E log V) using a priority queue
Space Complexity: O(V)
"""
import heapq
from typing import Dict, List, Tuple, Hashable

def dijkstra(graph: Dict[Hashable, List[Tuple[Hashable, float]]], start: Hashable) -> Dict[Hashable, float]:
    """Return a mapping of nodes to their minimum distance from *start*."""
    distances: Dict[Hashable, float] = {start: 0.0}
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
