def balance_binary_search_tree(root):
    """
    Balances an unbalanced binary search tree.
    Input: Root node of an unbalanced BST.
    Output: Root node of a balanced BST.
    """
    if root is None:
        return None
    
    # Step 1: Get the inorder traversal of the tree
    nodes = []
    in_order_traversal(root, nodes)

    # Step 2: Construct a balanced BST from the inorder traversal
    return construct_balanced_bst(nodes, 0, len(nodes) - 1)


def in_order_traversal(root, nodes):
    """
    Performs an inorder traversal of the tree and stores the nodes in a list.
    :param root: Current root node in the traversal.
    :param nodes: List to store the nodes.
    """
    if root is not None:
        in_order_traversal(root.left, nodes)
        nodes.append(root)
        in_order_traversal(root.right, nodes)


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