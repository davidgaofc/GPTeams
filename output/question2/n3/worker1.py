```python
def balance_binary_search_tree(root):
    """
    Balances an unbalanced binary search tree.
    Input: Root node of an unbalanced BST.
    Output: Root node of a balanced BST.
    """
    # Step 1: Convert the BST into a sorted list using inorder traversal
    def inorder_traversal(node, elements):
        if node:
            inorder_traversal(node.left, elements)
            elements.append(node.value)
            inorder_traversal(node.right, elements)
    
    elements = []
    inorder_traversal(root, elements)
    
    # Step 2: Create a new balanced BST from the sorted list
    def create_balanced_bst(elements, start, end):
        if start > end:
            return None
        
        mid = (start + end) // 2
        node = Node(elements[mid])
        
        node.left = create_balanced_bst(elements, start, mid - 1)
        node.right = create_balanced_bst(elements, mid + 1, end)
        
        return node
    
    return create_balanced_bst(elements, 0, len(elements) - 1)
```
The `balance_binary_search_tree` function first converts the unbalanced BST into a sorted list using inorder traversal. It then uses this sorted list to create a new balanced BST recursively by dividing the list into two halves and creating a node with the middle element as the root. The left half of the list is used to create the left subtree, and the right half of the list is used to create the right subtree. This process is repeated until all elements in the list have been processed. Finally, the root of the new balanced BST is returned.