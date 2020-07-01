class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def print_list(self):
        node = self
        output = ''
        while node is not None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    # Iterative Solution
    def reverse_recursively(self, head):
        # if head.next is not None:
        #     new_listnode = self.reverse_recursively(head.next)
        #     head.next.next = head
        #     head.next = None
        #     return new_listnode
        # else:
        #     return head
        return head

    def reverse_iteratively(self, head):
        vals = [head.val]
        while head.next is not None:
            head = head.next
            vals.append(head.val)
        vals = vals[::-1]
        new_node = ListNode(vals[0])
        current = new_node
        for val in vals[1:]:
            current.next = ListNode(val)
            current = current.next
        return new_node


# Implement this.

# Test Program
# Initialize the test list:
test_head = ListNode(4)
node1 = ListNode(3)
test_head.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
node3.next = ListNode(0)

print("Initial list:")
test_head.print_list()
result = test_head.reverse_iteratively(test_head)
print('Reversed list:')
result.print_list()
