def postorder(node):
    """Return post-order traversal of a binary tree.

    Complexity: Time O(n), Space O(n) recursion.
    """
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.value]
