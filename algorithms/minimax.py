class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children or []


def minimax(node, maximizing):
    """Compute minimax value of a game tree.

    Time: O(b^d), Space: O(d)
    """
    if not node.children:
        return node.value
    if maximizing:
        return max(minimax(c, False) for c in node.children)
    return min(minimax(c, True) for c in node.children)
