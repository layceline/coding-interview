# Implement an algorithm to find the kth to last element of a singly linked list
from linkedlist.linked_list import create_linked_list


def find_kth_to_last(linked_list, k):
    p1 = linked_list
    p2 = linked_list

    for _ in range(k):
        if p1.next is not None:
            p1 = p1.next
        else:
            return None

    while p1 is not None:
        p1 = p1.next
        p2 = p2.next
    return p2.data


if __name__ == '__main__':
    my_linked_list = create_linked_list(10)
    print(my_linked_list)
    print(find_kth_to_last(my_linked_list, 4))
