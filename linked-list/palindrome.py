# Implement a function to check if a linked list is a palindrome
from linkedlist.linked_list import Node, create_linked_list


def inverse_link_list(link_list, next_node=None):
    if link_list is None:
        return next_node
    node = Node(link_list.data)
    node.next = next_node
    prev_node = inverse_link_list(link_list.next, node)
    return prev_node


if __name__ == '__main__':
    input_linked_list = Node.from_list([0, 1, 2, 3, 0])
    print(inverse_link_list(input_linked_list))