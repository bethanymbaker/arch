class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        print(f'data = {self.data}')

    def append_to_tail(self):
        node = self
        while node.next is not None:
            node = node.next
        node.next = Node(2 * node.data)


if __name__ == '__main__':
    tmp = Node(42)
    tmp.append_to_tail()
    tmp.get_data()
