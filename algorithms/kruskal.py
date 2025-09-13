"""Kruskal's algorithm for minimum spanning tree.

Sorts edges by weight and adds them if they don't form a cycle, using Union-Find.
Time Complexity: O(E log E), where E is the number of edges.
Space Complexity: O(V), where V is the number of vertices.
"""

from .union_find import UnionFind
from typing import List, Tuple, Iterable, TypeVar

T = TypeVar("T")

def kruskal(vertices: Iterable[T], edges: List[Tuple[T, T, float]]) -> List[Tuple[T, T, float]]:
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

if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    edges = [
        ('A', 'B', 4), ('A', 'F', 2),
        ('B', 'C', 6), ('B', 'F', 5),
        ('C', 'D', 3), ('C', 'F', 1),
        ('D', 'E', 2),
        ('E', 'F', 4)
    ]
    mst = kruskal(vertices, edges)
    print("Edges in the Minimum Spanning Tree:")
    for u, v, w in mst:
        print(f"({u}, {v}, {w})")