```python
def balance_binary_search_tree(root):
    """
    Balances an unbalanced binary search tree.
    Input: Root node of an unbalanced BST.
    Output: Root node of a balanced BST.
    """
    # Step 1: Convert Binary Search Tree to Sorted List
    sorted_list = convert_bst_to_sorted_list(root)

    # Step 2: Convert Sorted List to Balanced Binary Search Tree
    balanced_root = convert_sorted_list_to_bst(sorted_list)

    return balanced_root


def convert_bst_to_sorted_list(root):
    """
    Helper function to convert Binary Search Tree to Sorted List.
    Input: Root node of the Binary Search Tree.
    Output: Sorted list representing the Binary Search Tree.
    """
    if root is None:
        return []

    sorted_list = convert_bst_to_sorted_list(root.left)
    sorted_list.append(root.value)
    sorted_list.extend(convert_bst_to_sorted_list(root.right))

    return sorted_list


def convert_sorted_list_to_bst(sorted_list):
    """
    Helper function to convert Sorted List to Binary Search Tree.
    Input: Sorted list representing the Binary Search Tree.
    Output: Root node of the Binary Search Tree.
    """
    if not sorted_list:
        return None

    mid = len(sorted_list) // 2
    root = TreeNode(sorted_list[mid])
    root.left = convert_sorted_list_to_bst(sorted_list[:mid])
    root.right = convert_sorted_list_to_bst(sorted_list[mid + 1:])

    return root
```

Explanation:
- The `balance_binary_search_tree` function takes the root node of an unbalanced binary search tree as input and returns the root node of a balanced binary search tree as output.
- The function first converts the binary search tree to a sorted list using the `convert_bst_to_sorted_list` helper function.
- Then, it converts the sorted list back to a balanced binary search tree using the `convert_sorted_list_to_bst` helper function.
- The `convert_bst_to_sorted_list` function recursively traverses the binary search tree in in-order (left, root, right) and appends the values to a list. This results in a sorted list representing the binary search tree.
- The `convert_sorted_list_to_bst` function takes a sorted list as input and recursively constructs a balanced binary search tree by selecting the middle element of the list as the root, then recursively calling the function on the left and right halves of the list to construct the left and right subtrees.