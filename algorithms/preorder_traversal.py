"""Pre-order traversal of a binary tree.

Visits nodes in the order: root, left subtree, right subtree.

Time complexity: O(n)
Space complexity: O(h) recursion depth
"""
from typing import Any, List, Optional


def preorder(node: Optional[Any]) -> List[Any]:
    """Return values visited by pre-order traversal.

    Accepts any node object with ``left``, ``right``, and ``value`` attributes.
    """
    if node is None:
        return []
    return [node.value] + preorder(node.left) + preorder(node.right)
