# Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the
# exact middle) of a singly linked list, given only access to that node

# Example
# input: the node c from the linked list a -> b -> c -> d -> e -> f
# result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f

from linkedlist.linked_list import create_linked_list


def delete_middle(node):
    node.data = node.next.data
    # hypothesis: we are in the middle
    node.next = node.next.next


if __name__ == '__main__':
    input = create_linked_list(10)
    print(input)
    delete_middle(input.next.next)
    print(input)
