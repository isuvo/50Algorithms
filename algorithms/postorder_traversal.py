"""Post-order traversal of a binary tree.

Visits nodes in the order: left subtree, right subtree, root.

Time complexity: O(n)
Space complexity: O(h) recursion depth
"""
from typing import Any, List, Optional


def postorder(node: Optional[Any]) -> List[Any]:
    """Return values visited by post-order traversal.

    Accepts any node object with ``left``, ``right``, and ``value`` attributes.
    """
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.value]
