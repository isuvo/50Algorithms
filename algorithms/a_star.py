"""
A* (A-star) search algorithm.

This implementation of the A* search algorithm finds the shortest path from a
start node to a goal node in a weighted graph. It uses a heuristic function to
estimate the cost of the cheapest path from a node to the goal.

Time Complexity: O(E log V), where V is the number of vertices and E is the
number of edges.
Space Complexity: O(V), where V is the number of vertices.
"""
from heapq import heappush, heappop
from typing import Dict, List, Tuple, Callable, TypeVar, Optional

T = TypeVar("T")

Graph = Dict[T, List[Tuple[T, float]]]
Heuristic = Callable[[T], float]

def a_star(graph: Graph[T], start: T, goal: T, heuristic: Heuristic[T]) -> Optional[Tuple[List[T], float]]:
    """
    A* pathfinding from start to goal.

    Args:
        graph: A dictionary mapping each node to a list of its neighbors and the
               cost of the edge to that neighbor.
        start: The starting node.
        goal: The goal node.
        heuristic: A function that estimates the distance from a node to the goal.

    Returns:
        A tuple containing the shortest path from the start to the goal and the
        cost of that path, or (None, inf) if no path is found.
    """
    open_set = [(heuristic(start), start, [start])]
    g: Dict[T, float] = {start: 0}
    while open_set:
        f, node, path = heappop(open_set)
        if node == goal:
            return path, g[node]
        for neigh, cost in graph.get(node, []):
            tentative = g[node] + cost
            if tentative < g.get(neigh, float('inf')):
                g[neigh] = tentative
                heappush(open_set, (tentative + heuristic(neigh), neigh, path + [neigh]))
    return None, float('inf')

if __name__ == "__main__":
    # Example: Find the shortest path in a simple graph
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    start_node = 'A'
    goal_node = 'D'

    def heuristic(node: str) -> float:
        # A simple heuristic for this example (manhattan distance if nodes were on a grid)
        goal_pos = {'A': (0, 0), 'B': (1, 1), 'C': (1, 0), 'D': (2, 0)}
        return abs(goal_pos[node][0] - goal_pos[goal_node][0]) + abs(goal_pos[node][1] - goal_pos[goal_node][1])

    path, cost = a_star(graph, start_node, goal_node, heuristic)
    if path:
        print(f"Shortest path from {start_node} to {goal_node}: {path}")
        print(f"Cost: {cost}")
    else:
        print(f"No path found from {start_node} to {goal_node}")