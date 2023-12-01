```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

class Tree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

def find_lowest_common_ancestor(tree, value1, value2):
    def find_node(node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        for child in node.children:
            if find_node(child, value):
                return True
        return False

    def find_common_ancestor(node, value1, value2):
        if node is None:
            return None

        if node.value == value1 or node.value == value2:
            return node.value

        child_values = []
        for child in node.children:
            value = find_common_ancestor(child, value1, value2)
            if value is not None:
                child_values.append(value)

        if len(child_values) == 2:
            return node.value
        elif len(child_values) == 1:
            return child_values[0]
        else:
            return None

    return find_common_ancestor(tree.root, value1, value2)
```

The function `find_lowest_common_ancestor` first defines two helper functions: `find_node` and `find_common_ancestor`. 

The `find_node` function recursively searches for a node with a specific value in the tree. It takes a `TreeNode` object and a value as input, and returns `True` if the value is found in the subtree rooted at the given node, and `False` otherwise.

The `find_common_ancestor` function recursively searches for the lowest common ancestor of two nodes with specific values in the tree. It takes a `TreeNode` object and two values as input, and returns the value of the lowest common ancestor if it exists, and `None` otherwise. 

Within the `find_common_ancestor` function, the function checks if the current node has one of the desired values. If it does, it returns the value. Otherwise, it recursively checks the children of the current node, and keeps track of the values found in the children. 

Finally, the `find_lowest_common_ancestor` function calls `find_common_ancestor` starting from the root of the tree, and returns the value of the lowest common ancestor.