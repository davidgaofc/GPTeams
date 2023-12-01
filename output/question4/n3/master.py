class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self

class Tree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

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

    # Find the nodes with the given values
    node1 = tree.root.find_node(tree.root, value1)
    node2 = tree.root.find_node(tree.root, value2)

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