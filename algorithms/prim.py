"""Prim's algorithm for minimum spanning tree.

Grows the MST by attaching the nearest vertex using a priority queue.
Time Complexity: O(E log V), where V is the number of vertices and E is the
number of edges.
Space Complexity: O(V), where V is the number of vertices.
"""

import heapq
from typing import Dict, List, Tuple, Hashable

Graph = Dict[Hashable, List[Tuple[Hashable, float]]]

def prim(graph: Graph, start: Hashable) -> List[Tuple[Hashable, Hashable, float]]:
    """Return the edges in the minimum spanning tree of *graph* starting from *start*.

    *graph* maps vertices to iterables of (neighbor, weight).
    """
    if start not in graph:
        return []
    visited = {start}
    edges: List[Tuple[float, Hashable, Hashable]] = []
    for v, w in graph[start]:
        heapq.heappush(edges, (w, start, v))
    mst = []
    while edges and len(visited) < len(graph):
        w, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, w))
            for nv, nw in graph[v]:
                if nv not in visited:
                    heapq.heappush(edges, (nw, v, nv))
    return mst

if __name__ == "__main__":
    graph = {
        'A': [('B', 4), ('F', 2)],
        'B': [('A', 4), ('C', 6), ('F', 5)],
        'C': [('B', 6), ('D', 3), ('F', 1)],
        'D': [('C', 3), ('E', 2)],
        'E': [('D', 2), ('F', 4)],
        'F': [('A', 2), ('B', 5), ('C', 1), ('E', 4)]
    }
    start_node = 'A'
    mst = prim(graph, start_node)
    print("Edges in the Minimum Spanning Tree:")
    for u, v, w in mst:
        print(f"({u}, {v}, {w})")