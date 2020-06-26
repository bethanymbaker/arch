# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


class Node:

    def __init__(self, data):
        self.data = data
        self.child = None
        self.has_child = False

    def set_child(self, node):
        self.child = node
        self.has_child = True

    def append_node(self, node):
        current = self
        while current.has_child:
            current = current.child
        current.set_child(node)

    def get_children(self):
        children = []
        current = self
        children.append(str(current.data))
        while current.has_child:
            current = current.child
            children.append(str(current.data))
        return children

    def print_node(self):
        print(f"({' -> '.join(self.get_children())})")

    def add_node(self, node_2):
        node_val_1 = int(''.join(self.get_children()[::-1]))
        node_val_2 = int(''.join(node_2.get_children()[::-1]))
        summ = list(str(node_val_1 + node_val_2))[::-1]
        new_list = Node(summ[0])
        if len(summ) > 1:
            for val in summ[1:]:
                new_list.append_node(Node(val))
        return new_list


if __name__ == '__main__':
    list_1 = Node(2)
    list_1.append_node(Node(4))
    list_1.append_node(Node(3))

    list_2 = Node(5)
    list_2.append_node(Node(6))
    list_2.append_node(Node(4))

    new_node = list_1.add_node(list_2)
    new_node.print_node()
    # print(f'sum = {list_1.add_node(list_2)}')
