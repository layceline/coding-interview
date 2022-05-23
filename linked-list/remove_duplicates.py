# Write code to remove duplicates from an unsorted linked list.
# Follow up: How would you solve this problem if a temporary buffer is not allowed
from linkedlist.linked_list import create_linked_list


def remove_duplicates(linked_list):
    if linked_list is None:
        return None

    values = set()
    values.add(linked_list.data)

    while linked_list is not None and linked_list.next is not None:
        if linked_list.next.data in values:
            linked_list.next = linked_list.next.next
        else:
            values.add(linked_list.next.data)
            linked_list = linked_list.next


if __name__ == '__main__':
    my_linked_list = create_linked_list(10)
    my_linked_list.print()
    remove_duplicates(my_linked_list)
    my_linked_list.print()
