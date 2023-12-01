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
    path1 = find_path(tree.root, value1)
    path2 = find_path(tree.root, value2)

    if path1 is None or path2 is None:
        return None

    # Find the index of the first different value in the paths
    i = 0
    while i < len(path1) and i < len(path2) and path1[i] == path2[i]:
        i += 1

    # Return the value of the common ancestor
    return path1[i - 1]


def find_path(node, value):
    if node.value == value:
        return [node.value]

    for child in node.children:
        path = find_path(child, value)
        if path is not None:
            path.insert(0, node.value)
            return path

    return None