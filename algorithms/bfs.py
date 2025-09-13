"""
Breadth-first search (BFS).

BFS explores a graph level by level starting from a source node using a queue.
It visits all nodes at the current depth before moving to the next level.

Time Complexity: O(V + E), where V is the number of vertices and E is the
number of edges.
Space Complexity: O(V), where V is the number of vertices.
"""
from collections import deque
from typing import Dict, List, Hashable

Graph = Dict[Hashable, List[Hashable]]

def bfs(graph: Graph, start: Hashable) -> List[Hashable]:
    """Return list of nodes visited in BFS order starting from *start*."""
    if start not in graph:
        return []
    visited = {start}
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
    traversal = bfs(graph, start_node)
    print(f"BFS traversal starting from {start_node}: {traversal}")