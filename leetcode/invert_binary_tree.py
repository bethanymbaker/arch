class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def preorder(self):
        print(self.value)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()


def invert(node):
    new_left, new_right = None, None
    if node.left:
        new_left = invert(node.left)
    if node.right:
        new_right = invert(node.right)
    node.left = new_right
    node.right = new_left
    return node


# Fill this in.

root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.left = Node('f')

root.preorder()
# a b d e c f
print("\n")
invert(root)
root.preorder()
# a c f b e d
