from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

class Tree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def add_node(self, parent_value, child_value):
        parent_node = self.find_node(self.root, parent_value)
        if parent_node is not None:
            parent_node.add_child(TreeNode(child_value))

    def find_node(self, node, value):
        if node.value == value:
            return node
        for child in node.children:
            found = self.find_node(child, value)
            if found:
                return found
        return None

    def traverse_bfs(self):
        visited = []
        queue = deque([self.root])
        while queue:
            current_node = queue.popleft()
            visited.append(current_node.value)
            queue.extend(current_node.children)
        return visited

def create_tree(root_value):
    return Tree(root_value)

def add_node_to_tree(tree, parent_value, child_value):
    tree.add_node(parent_value, child_value)

# TODO: Implement 'find_lowest_common_ancestor'
def find_lowest_common_ancestor(tree, value1, value2):
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
    return ancestors1[i + 1].value