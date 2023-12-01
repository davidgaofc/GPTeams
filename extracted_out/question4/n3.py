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
    # This function should take a Tree object and two node values, and find the lowest common ancestor (LCA) of these nodes.
    # The LCA is the lowest node in the tree that has both nodes as descendants (where we allow a node to be a descendant of itself).
    # Expected Input: tree (Tree object), value1 (node value), value2 (node value)
    # Expected Output: lca_value (value of the lowest common ancestor node)
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