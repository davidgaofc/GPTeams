```python
def balance_binary_search_tree(root):
    """
    Balances an unbalanced binary search tree.
    Input: Root node of an unbalanced BST.
    Output: Root node of a balanced BST.
    """
    if root is None:
        return None
    
    # Create a sorted list of all nodes in the tree
    nodes = in_order_traversal(root)
    
    # Construct a new balanced binary search tree from the sorted list of nodes
    return construct_balanced_bst(nodes)


def in_order_traversal(root):
    """
    Performs in-order traversal of the tree and returns a list of nodes.
    """
    if root is None:
        return []
    
    nodes = []
    nodes.extend(in_order_traversal(root.left))
    nodes.append(root)
    nodes.extend(in_order_traversal(root.right))
    
    return nodes


def construct_balanced_bst(nodes):
    """
    Constructs a balanced binary search tree from a sorted list of nodes.
    """
    if not nodes:
        return None
    
    mid = len(nodes) // 2
    node = nodes[mid]
    
    node.left = construct_balanced_bst(nodes[:mid])
    node.right = construct_balanced_bst(nodes[mid+1:])
    
    return node
```

