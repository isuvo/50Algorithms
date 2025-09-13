"""
Depth-first search (DFS).

DFS explores as far as possible along each branch before backtracking. It can be
implemented recursively or using a stack. This implementation uses recursion.

Time Complexity: O(V + E), where V is the number of vertices and E is the
number of edges.
Space Complexity: O(V) due to recursion stack, where V is the number of
vertices.
"""
from typing import Dict, List, Hashable

Graph = Dict[Hashable, List[Hashable]]

def dfs(graph: Graph, start: Hashable) -> List[Hashable]:
    """Return list of nodes visited in DFS order starting from *start*."""
    if start not in graph:
        return []
    visited: set[Hashable] = set()
    order: List[Hashable] = []
    def _visit(node: Hashable) -> None:
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                _visit(neighbor)
    _visit(start)
    return order

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    start_node = 'A'
    traversal = dfs(graph, start_node)
    print(f"DFS traversal starting from {start_node}: {traversal}")