# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_num(l1):
    num_1 = []

    val = l1.val
    num_1.append(val)

    next_list_node = l1.next

    if next_list_node is not None:
        while next_list_node.next is not None:
            val = next_list_node.val
            num_1.append(val)
            next_list_node = next_list_node.next
        num_1.append(next_list_node.val)
    rev_str_list = [str(i) for i in num_1[::-1]]
    return int(''.join(rev_str_list))


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num_1 = get_num(l1)
        num_2 = get_num(l2)
        target = str(num_1 + num_2)
        new_lst = [int(i) for i in list(target)]
        link_node = ListNode(x=new_lst[0])
        for digitt in new_lst[1:]:
            new_link_node = ListNode(x=digitt)
            new_link_node.next = link_node
            link_node = new_link_node
        return link_node


def list_to_link_node(lst):
    pass

if __name__ == '__main__':
    lst_1 = [2, 4, 3]
    lst_2 = [5, 6, 4]
    pass
