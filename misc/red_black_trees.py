from enum import Enum

class Color(Enum):
    RED = 1
    BLACK = 2

# Every node is either red or black.
# Every leaf (NULL) is black.
# If a node is red, then both its children are black.
# Every simple path from a node to a descendant leaf contains the same number of black nodes.
class Tree:
    def __init__(self, root):
        self.root = root


# The number of black nodes on any path from, but not including, 
# a node x to a leaf is called the black-height of a node, denoted bh(x).
class Node:
    def __init__(self, color, value, parent):
        self.color = color
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

def insert(parent, value):
    if parent.value > value:
        left = parent.left
        if not left:
            parent.left = Node(Color.RED, value, parent)
            return parent.left
        else:
            return insert(parent.left, value)
    else:
        right = parent.right
        if not right:
            parent.right = Node(Color.RED, value, parent)
            return parent.right
        else:
            return insert(parent.right, value)


def insert_rb(tree, value):
    node = insert(tree.root, value)
    while tree.root is not node and node.parent.color is Color.RED:

        if node.parent is node.parent.parent.left:
            uncle = node.parent.parent.right # right uncle if parent is left

            if uncle.color is Color.RED:
                # Case 1 - Change colors
                node.parent.parent.color = Color.RED
                node.parent.color = Color.BLACK
                uncle.color = Color.BLACK

                node = node.parent.parent # Move head
            else:
                if node is node.parent.right:
                    # Case 2 - move node up and rotate
                    node = node.parent
                    rotate_left(tree, node)
                else:
                    # Case 3
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                    rotate_right(tree, node)
        else:
            uncle = node.parent.parent.left

            if uncle.color is Color.RED:
                # Case 1 - Change colors
                node.parent.parent.color = Color.RED
                node.parent.color = Color.BLACK
                uncle.color = Color.BLACK

                node = node.parent.parent # Move head
            else:
                if node is node.parent.left:
                    # Case 2 - move node up and rotate
                    node = node.parent
                    rotate_right(tree, node)
                else:
                    # Case 3
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                    rotate_left(tree, node)

    tree.root.color = Color.BLACK

