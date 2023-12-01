```python
def find_lowest_common_ancestor(tree, value1, value2):
    def traverse(node, value1, value2):
        if node is None:
            return None

        if node.value == value1 or node.value == value2:
            return node

        left_LCA = traverse(node.left, value1, value2)
        right_LCA = traverse(node.right, value1, value2)

        if left_LCA and right_LCA:
            return node

        return left_LCA if left_LCA else right_LCA

    return traverse(tree.root, value1, value2).value
```