"""
Depth-first search (DFS).

DFS explores as far as possible along each branch before backtracking. It can be
implemented recursively or using a stack. This implementation uses recursion.

Time Complexity: O(V + E)
Space Complexity: O(V) due to recursion stack
"""
from typing import Dict, List, Hashable

def dfs(graph: Dict[Hashable, List[Hashable]], start: Hashable) -> List[Hashable]:
    """Return list of nodes visited in DFS order starting from *start*."""
    visited = set()
    order: List[Hashable] = []
    def _visit(node: Hashable) -> None:
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                _visit(neighbor)
    _visit(start)
    return order
