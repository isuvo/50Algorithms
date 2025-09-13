"""
Topological sort for directed acyclic graphs (DAGs).

This implementation uses Kahn's algorithm to repeatedly remove nodes with zero
in-degree, producing a linear ordering where each node appears before all nodes
it points to.

Time Complexity: O(V + E), where V is the number of vertices and E is the
number of edges.
Space Complexity: O(V), where V is the number of vertices.
"""
from collections import deque
from typing import Dict, List, Hashable

Graph = Dict[Hashable, List[Hashable]]

def topological_sort(graph: Graph) -> List[Hashable]:
    """Return a list of nodes in topologically sorted order."""
    in_degree: Dict[Hashable, int] = {node: 0 for node in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] = in_degree.get(v, 0) + 1

    queue = deque([node for node, deg in in_degree.items() if deg == 0])
    order: List[Hashable] = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph.get(u, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(order) != len(in_degree):
        raise ValueError("Graph has at least one cycle")
    return order

if __name__ == "__main__":
    graph = {
        'A': ['C'],
        'B': ['C', 'D'],
        'C': ['E'],
        'D': ['F'],
        'E': ['F'],
        'F': []
    }
    sorted_order = topological_sort(graph)
    print(f"Topological sort of the graph: {sorted_order}")