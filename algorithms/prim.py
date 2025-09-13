"""Prim's algorithm for minimum spanning tree.

Grows the MST by attaching the nearest vertex using a priority queue.
Time Complexity: O(E log V)
Space Complexity: O(V)
"""

import heapq

def prim(graph, start):
    """Return the edges in the minimum spanning tree of *graph* starting from *start*.

    *graph* maps vertices to iterables of (neighbor, weight).
    """
    visited = {start}
    edges = []
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
