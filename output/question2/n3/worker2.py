```python
def balance_binary_search_tree(root):
    """
    Balances an unbalanced binary search tree.
    Input: Root node of an unbalanced BST.
    Output: Root node of a balanced BST.
    """
    # Step 1: Get the inorder traversal of the tree
    nodes = []
    inorder_traversal(root, nodes)

    # Step 2: Construct a balanced BST from the inorder traversal
    return construct_balanced_bst(nodes, 0, len(nodes) - 1)


def inorder_traversal(node, nodes):
    """
    Performs an inorder traversal of the tree and stores the nodes in a list.
    :param node: Current node in the traversal.
    :param nodes: List to store the nodes.
    """
    if node is not None:
        inorder_traversal(node.left, nodes)
        nodes.append(node)
        inorder_traversal(node.right, nodes)


def construct_balanced_bst(nodes, start, end):
    """
    Constructs a balanced BST from the sorted nodes list.
    :param nodes: List of nodes.
    :param start: Start index of the sublist.
    :param end: End index of the sublist.
    :return: Root node of the balanced BST.
    """
    if start > end:
        return None
    mid = (start + end) // 2
    root = nodes[mid]
    root.left = construct_balanced_bst(nodes, start, mid - 1)
    root.right = construct_balanced_bst(nodes, mid + 1, end)
    return root
```

The `balance_binary_search_tree` function takes the root node of an unbalanced binary search tree as input and returns the root node of a balanced binary search tree. It uses the `inorder_traversal` function to obtain the inorder traversal of the unbalanced tree and then uses the `construct_balanced_bst` function to construct a balanced binary search tree from the sorted nodes list.

The `inorder_traversal` function performs an inorder traversal of the tree and stores the nodes in a list. It is a helper function for `balance_binary_search_tree`.

The `construct_balanced_bst` function constructs a balanced binary search tree from the sorted nodes list. It uses a recursive approach by dividing the nodes list into two sublists and recursively constructing the left and right subtrees.

Note: This code assumes that the `Node` class has `left`, `right`, and `value` attributes. The code provided in the question does not include the definition of the `Node` class, so you may need to modify the code accordingly.