class TreeNode:
    """
    Node class for Binary Search Tree.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_into_bst(root, value):
    """
    Inserts a value into the BST.
    :param root: Root node of the BST.
    :param value: Value to insert.
    :return: Root node after insertion.
    """
    if root is None:
        return TreeNode(value)
    else:
        if value < root.value:
            root.left = insert_into_bst(root.left, value)
        else:
            root.right = insert_into_bst(root.right, value)
    return root

def create_binary_search_tree(data):
    """
    Constructs a binary search tree from the data.
    :param data: List of values.
    :return: Root of the binary search tree.
    """
    root = None
    for value in data:
        root = insert_into_bst(root, value)
    return root

def tree_height(root):
    """
    Computes the height of the tree.
    :param root: Root node of the tree.
    :return: Height of the tree.
    """
    if root is None:
        return 0
    return max(tree_height(root.left), tree_height(root.right)) + 1

def analyze_tree_balance(root):
    """
    Analyzes the balance of the BST.
    :param root: Root node of the BST.
    :return: Balance information of the tree.
    """
    if root is None:
        return 0
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    return left_height - right_height

def display_tree(root, level=0, prefix="Root: "):
    """
    Displays the structure of the tree.
    :param root: Root node of the tree.
    :param level: Current level in the tree.
    :param prefix: Prefix string for display.
    """
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.value))
        if root.left is not None or root.right is not None:
            if root.left:
                display_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                display_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

def search_in_tree(root, value):
    """
    Searches for a value in the BST.
    :param root: Root node of the BST.
    :param value: Value to search for.
    :return: True if value is found, else False.
    """
    if root is None:
        return False
    if root.value == value:
        return True
    elif value < root.value:
        return search_in_tree(root.left, value)
    else:
        return search_in_tree(root.right, value)

# TODO: Implement balance_binary_search_tree function
def balance_binary_search_tree(root):
    """
    Balances an unbalanced binary search tree.
    Input: Root node of an unbalanced BST.
    Output: Root node of a balanced BST.
    """
    # Step 1: Convert Binary Search Tree to Sorted List
    sorted_list = convert_bst_to_sorted_list(root)

    # Step 2: Convert Sorted List to Balanced Binary Search Tree
    balanced_root = convert_sorted_list_to_bst(sorted_list)

    return balanced_root


def convert_bst_to_sorted_list(root):
    """
    Helper function to convert Binary Search Tree to Sorted List.
    Input: Root node of the Binary Search Tree.
    Output: Sorted list representing the Binary Search Tree.
    """
    if root is None:
        return []

    sorted_list = convert_bst_to_sorted_list(root.left)
    sorted_list.append(root.value)
    sorted_list.extend(convert_bst_to_sorted_list(root.right))

    return sorted_list


def convert_sorted_list_to_bst(sorted_list):
    """
    Helper function to convert Sorted List to Binary Search Tree.
    Input: Sorted list representing the Binary Search Tree.
    Output: Root node of the Binary Search Tree.
    """
    if not sorted_list:
        return None

    mid = len(sorted_list) // 2
    root = TreeNode(sorted_list[mid])
    root.left = convert_sorted_list_to_bst(sorted_list[:mid])
    root.right = convert_sorted_list_to_bst(sorted_list[mid + 1:])

    return root

def load_data():
    """
    Simulates loading data from a file.
    :return: List of data items.
    """
    return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

