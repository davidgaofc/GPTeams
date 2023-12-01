```python
def find_lowest_common_ancestor(tree, value1, value2):
    def find_ancestors(node, value, ancestors):
        if node is None:
            return False
        ancestors.append(node.value)
        if node.value == value:
            return True
        for child in node.children:
            if find_ancestors(child, value, ancestors):
                return True
        ancestors.pop()
        return False
    
    ancestors1 = []
    find_ancestors(tree.root, value1, ancestors1)
    
    ancestors2 = []
    find_ancestors(tree.root, value2, ancestors2)
    
    lca_value = None
    for i in range(min(len(ancestors1), len(ancestors2))):
        if ancestors1[i] == ancestors2[i]:
            lca_value = ancestors1[i]
        else:
            break
    
    return lca_value
```
In this implementation, we define a helper function called `find_ancestors` that finds the ancestors of a given node in the tree. It takes a node, a value, and a list of ancestors as arguments. It traverses the tree recursively, adding the value of each visited node to the list of ancestors, until it finds the node with the given value. If the node is found, it returns True to indicate that the value was found, otherwise it returns False. 

In the `find_lowest_common_ancestor` function, we call `find_ancestors` twice, once for `value1` and once for `value2`, to find the ancestors of both nodes. We then iterate through the lists of ancestors starting from the root of the tree, comparing the values at each position. If the values are the same, we update the `lca_value` variable with the common ancestor. If the values are different, we break out of the loop because we have found the lowest common ancestor. Finally, we return the `lca_value`.