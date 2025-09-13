from heapq import heappush, heappop


def a_star(graph, start, goal, heuristic):
    """A* pathfinding from start to goal.

    Args:
        graph: dict mapping node -> iterable of (neighbor, cost).
        start: starting node.
        goal: goal node.
        heuristic: function estimating distance from a node to the goal.
    Returns:
        (path, cost) where path is a list of nodes.
    Complexity:
        Time O(E log V), Space O(V)
    """
    open_set = [(heuristic(start), start, [start])]
    g = {start: 0}
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
