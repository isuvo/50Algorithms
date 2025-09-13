"""In-order traversal of a binary tree.

Visits nodes in the order: left subtree, root, right subtree.

Time complexity: O(n)
Space complexity: O(h) recursion depth
"""
from typing import Any, List, Optional


def inorder(node: Optional[Any]) -> List[Any]:
    """Return values visited by in-order traversal.

    Accepts any node object with ``left``, ``right``, and ``value`` attributes.
    """
    if node is None:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)
