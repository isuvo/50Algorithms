def preorder(node):
    """Return pre-order traversal of a binary tree.

    Complexity: Time O(n), Space O(n) recursion.
    """
    if node is None:
        return []
    return [node.value] + preorder(node.left) + preorder(node.right)
