def balance_binary_search_tree(root):
    """
    Balances an unbalanced binary search tree.
    Input: Root node of an unbalanced BST.
    Output: Root node of a balanced BST.
    """

    # Step 1: Extract the values from the tree in sorted order
    values = extract_values(root)

    # Step 2: Create a balanced BST from the sorted values
    return create_balanced_bst(values)

def extract_values(root):
    """
    Extracts the values from the tree in sorted order.
    """
    if root is None:
        return []
    return extract_values(root.left) + [root.value] + extract_values(root.right)

def create_balanced_bst(values):
    """
    Creates a balanced BST from the sorted values.
    """
    if not values:
        return None

    mid = len(values) // 2
    root = Node(values[mid])
    root.left = create_balanced_bst(values[:mid])
    root.right = create_balanced_bst(values[mid+1:])

    return root