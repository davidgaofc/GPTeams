def find_lowest_common_ancestor(tree, value1, value2):
    # Find the nodes with the given values
    node1 = tree.find_node(tree.root, value1)
    node2 = tree.find_node(tree.root, value2)
    
    # If either node is not found, return None
    if node1 is None or node2 is None:
        return None
    
    # Create lists to store the ancestors of each node
    ancestors1 = [node1]
    ancestors2 = [node2]
    
    # Traverse up from node1 to the root and store all ancestors in ancestors1
    current_node = node1
    while current_node != tree.root:
        current_node = tree.find_node(tree.root, current_node.value)
        ancestors1.append(current_node)
    
    # Traverse up from node2 to the root and store all ancestors in ancestors2
    current_node = node2
    while current_node != tree.root:
        current_node = tree.find_node(tree.root, current_node.value)
        ancestors2.append(current_node)
    
    # Find the lowest common ancestor by traversing both lists from the end
    i = -1
    while i >= -len(ancestors1) and i >= -len(ancestors2) and ancestors1[i] == ancestors2[i]:
        i -= 1
    
    # Return the value of the lowest common ancestor
    return ancestors1[i+1].value