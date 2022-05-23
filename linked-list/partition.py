# Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater
# than or equal to x. (IMPORTANT: The partition element x can appear anywhere in the "right partition"; it does not need
# to appear between the left and the right partitions. The additional spacing in the example below indicates the
# partition. Yes, the output below is one of many valid outputs!)

# Example
# input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition=5]
# output: 3 -> 1 -> 2       ->         10 -> 5 -> 5 -> 8
from random import randint

from linkedlist.linked_list import create_linked_list, Node


def partition(linked_list, p):
    print(f"Partition is: {p}")
    smaller_than = None
    bigger_than = None
    while linked_list is not None:
        if linked_list.data < p:
            if smaller_than is None:
                smaller_than = Node(linked_list.data)
                first_smaller_than = smaller_than
            else:
                smaller_than.next = Node(linked_list.data)
                smaller_than = smaller_than.next
        else:
            if bigger_than is None:
                bigger_than = Node(linked_list.data)
                first_bigger_than = bigger_than
            else:
                bigger_than.next = Node(linked_list.data)
                bigger_than = bigger_than.next
        linked_list = linked_list.next

    if smaller_than is not None:
        smaller_than.next = first_bigger_than
    else:
        first_smaller_than = first_bigger_than

    return first_smaller_than


if __name__ == '__main__':
    input = create_linked_list(10)
    print(input)
    output = partition(input, randint(0, 5))
    print(output)
