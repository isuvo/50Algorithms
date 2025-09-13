def inorder(node):
    """Return in-order traversal of a binary tree.

    Args:
        node: root node with 'value', 'left', 'right'.
    Returns:
        List of visited values.
    Complexity: Time O(n), Space O(n) recursion.
    """
    if node is None:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)
