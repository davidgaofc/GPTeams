```python
def find_lowest_common_ancestor(tree, value1, value2):
    # Get the paths from the root to value1 and value2
    path1 = find_path(tree.root, value1)
    path2 = find_path(tree.root, value2)
    
    if path1 is None or path2 is None:
        return None
    
    # Find the index of the first different value in the paths
    i = 0
    while i < len(path1) and i < len(path2) and path1[i] == path2[i]:
        i += 1
    
    # Return the value of the common ancestor
    return path1[i-1]

def find_path(node, value):
    if node.value == value:
        return [node.value]
    
    for child in node.children:
        path = find_path(child, value)
        if path is not None:
            path.insert(0, node.value)
            return path
    
    return None
```

Note: This implementation assumes that the given values exist in the tree. If any of the values does not exist, it will return None.