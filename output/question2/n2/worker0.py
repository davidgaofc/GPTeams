Here is one possible implementation for the `balance_binary_search_tree` function:

```python
def balance_binary_search_tree(root):
    """
    Balances an unbalanced binary search tree.
    :param root: Root node of an unbalanced BST.
    :return: Root node of a balanced BST.
    """
    # Step 1: Convert the BST into a sorted array
    sorted_array = bst_to_sorted_array(root)

    # Step 2: Construct a balanced BST from the sorted array
    return sorted_array_to_bst(sorted_array)

def bst_to_sorted_array(root):
    """
    Converts a BST into a sorted array.
    :param root: Root node of the BST.
    :return: Sorted array representation of the BST.
    """
    sorted_array = []
    inorder_traversal(root, sorted_array.append)
    return sorted_array

def inorder_traversal(node, visit_func):
    """
    Perform inorder traversal on a BST and apply a visit function to each node.
    :param node: Root node of the BST.
    :param visit_func: Function to apply to each node.
    """
    if node is None:
        return
    inorder_traversal(node.left, visit_func)
    visit_func(node)
    inorder_traversal(node.right, visit_func)

def sorted_array_to_bst(sorted_array):
    """
    Constructs a balanced BST from a sorted array.
    :param sorted_array: Sorted array.
    :return: Root node of the balanced BST.
    """
    if not sorted_array:
        return None
    mid = len(sorted_array) // 2
    root = TreeNode(sorted_array[mid])
    root.left = sorted_array_to_bst(sorted_array[:mid])
    root.right = sorted_array_to_bst(sorted_array[mid+1:])
    return root
```

This implementation utilizes the following steps:
1. Convert the unbalanced BST into a sorted array by performing an inorder traversal and storing the values in an array.
2. Construct a balanced BST from the sorted array by recursively finding the middle element and setting it as the root, then constructing the left subtree and right subtree.

Note that we need two additional helper functions: `bst_to_sorted_array` and `inorder_traversal`. The `bst_to_sorted_array` function converts the BST into a sorted array, and the `inorder_traversal` function performs an inorder traversal on the BST and applies a visit function to each node.

Let me know if you have any questions!