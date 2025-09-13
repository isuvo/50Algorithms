"""
Breadth-first search (BFS).

BFS explores a graph level by level starting from a source node using a queue.
It visits all nodes at the current depth before moving to the next level.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""
from collections import deque
from typing import Dict, List, Hashable

def bfs(graph: Dict[Hashable, List[Hashable]], start: Hashable) -> List[Hashable]:
    """Return list of nodes visited in BFS order starting from *start*."""
    visited = set([start])
    queue = deque([start])
    order: List[Hashable] = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
