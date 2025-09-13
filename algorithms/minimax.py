"""Minimax algorithm for game trees.

Finds the optimal value assuming both players play optimally.

Time complexity: O(b^d)
Space complexity: O(d)
"""
from __future__ import annotations
from typing import List, Optional

class Node:
    """A node in a game tree."""
    def __init__(self, value: Optional[int] = None, children: Optional[List[Node]] = None):
        self.value = value
        self.children = children or []

def minimax(node: Node, maximizing: bool) -> int:
    """
    Compute the minimax value of a game tree.

    Args:
        node: The root node of the game tree.
        maximizing: Whether the current player is maximizing or minimizing.

    Returns:
        The minimax value of the game tree.
    """
    if not node.children:
        return node.value
    if maximizing:
        return max(minimax(c, False) for c in node.children)
    return min(minimax(c, True) for c in node.children)
