```python
def find_lowest_common_ancestor(tree, value1, value2):
    # Find the nodes with the given values
    node1 = tree.find_node(tree.root, value1)
    node2 = tree.find_node(tree.root, value2)

    # If any of the nodes is not found, return None
    if node1 is None or node2 is None:
        return None

    # Initialize a set to keep track of visited nodes
    visited = set()

    # Traverse from node1 to the root and mark visited nodes
    while node1 is not None:
        visited.add(node1.value)
        node1 = node1.parent

    # Traverse from node2 to the root until a visited node is found
    while node2 is not None:
        if node2.value in visited:
            return node2.value
        node2 = node2.parent

    # If no common ancestor is found, return None
    return None
```

Explanation:
The `find_lowest_common_ancestor` function takes a `tree` object, `value1` and `value2` as input. It first finds the nodes with the given values using the `find_node` method of the tree.

Next, it initializes a set called `visited` to keep track of the visited nodes. Then it traverses from `node1` to the root, adding each visited node's value to the `visited` set.

Finally, it traverses from `node2` to the root and checks if the value of the current node is in the `visited` set. If a common ancestor is found, it returns the value of that node. If no common ancestor is found, it returns `None`.

Note: This solution assumes that the parent nodes have a `parent` attribute that points to their parent node.