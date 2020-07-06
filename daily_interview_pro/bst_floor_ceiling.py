import numpy as np


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def find_ceiling_floor(root_node, k):
    return find_floor(root_node, k), find_ceiling(root_node, k)


def find_ceiling(root_node, k):
    if root_node.value == k:
        return k
    elif root_node.value > k:
        if root_node.left is not None:
            return np.min([find_ceiling(root_node.left, k), root_node.value])
        else:
            return root_node.value
    elif root_node.value < k:
        if root_node.right is not None:
            return find_ceiling(root_node.right, k)
        else:
            return np.inf


def find_floor(root_node, k):
    if root_node.value == k:
        return k
    if root_node.value < k:
        if root_node.right is not None:
            return np.max([find_floor(root_node.right, k), root_node.value])
        else:
            return root_node.value
    if root_node.value > k:
        if root_node.left is not None:
            return find_floor(root_node.left, k)
        else:
            return -np.inf


# Fill this in.
root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

for i in range(16):
    print(f'{find_floor(root, i)}-{i}-{find_ceiling(root, i)}')
