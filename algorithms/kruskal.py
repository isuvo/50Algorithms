"""Kruskal's algorithm for minimum spanning tree.

Sorts edges by weight and adds them if they don't form a cycle, using Union-Find.
Time Complexity: O(E log E)
Space Complexity: O(V)
"""

from .union_find import UnionFind

def kruskal(vertices, edges):
    """Return the edges in the minimum spanning tree using Kruskal's algorithm.

    *vertices* is an iterable of vertices; *edges* is an iterable of (u, v, w).
    """
    uf = UnionFind(vertices)
    mst = []
    for u, v, w in sorted(edges, key=lambda x: x[2]):
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
    return mst
