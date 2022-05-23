# You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in
# reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and
# returns the sun as a linked list. (You are not allowed to "cheat" and just convert the linked list to integer)

# Example
# input: (7 -> 1 -> 6) + {5 -> 9 -> 2). That is 617 + 295.
# output: 2 -> 1 -> 9. That is 912.
from random import randint

# Follow up
# Suppose the digits are stored in forward order. Repeat the above problem
# Example
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is 617 + 295.
# Output: 9 -> 1 -> 2. That is, 912.

from linkedlist.linked_list import create_linked_list, Node


def sum(nb1, nb2):
    carry = (nb1.data + nb2.data) // 10
    output = Node((nb1.data + nb2.data) % 10)
    first_output = output

    while nb1 is not None or nb2 is not None:
        if nb1 is not None:
            nb1 = nb1.next
        if nb2 is not None:
            nb2 = nb2.next

        if nb1 is not None and nb2 is not None:
            output.next = Node((nb1.data + nb2.data + carry) % 10)
            carry = (nb1.data + nb2.data + carry) // 10
            output = output.next
        else:
            if nb1 is not None:
                val = nb1.data
                output.next = Node((val + carry) % 10)
                carry = (val + carry) // 10
                output = output.next
            elif nb2 is not None:
                val = nb2.data
                output.next = Node((val + carry) % 10)
                carry = (val + carry) // 10
                output = output.next

    if carry > 0:
        output.next = Node(carry)

    return first_output


def recursive_sum(nb1, nb2, current_carry=0):
    if nb1 is None and nb2 is None:
        if current_carry > 0:
            return Node(current_carry)
        else:
            return None

    nb1 = nb1 or Node(0)
    nb2 = nb2 or Node(0)
    output = Node((nb1.data + nb2.data + current_carry) % 10)
    next_carry = (nb1.data + nb2.data + current_carry) // 10
    output.next = recursive_sum(nb1.next, nb2.next, next_carry)
    return output


def recursive_inverse_sum(nb1, nb2):
    # initialization for linked list of different size
    head_nb1 = nb1
    head_nb2 = nb2
    while nb1 is not None and nb2 is not None:
        nb1 = nb1.next
        nb2 = nb2.next

    if nb1 is None:
        while nb2 is not None:
            nb2 = nb2.next
            head_nb1 = Node(0, head_nb1)
    if nb2 is None:
        while nb1 is not None:
            nb1 = nb1.next
            head_nb2 = Node(0, head_nb2)
    node, carry = inverse_sum(head_nb1, head_nb2)
    if carry > 0:
        return Node(carry, node)
    else:
        return node


def inverse_sum(nb1, nb2):
    if nb1.next is None and nb2.next is None:
        next_node, next_carry = None, 0
    else:
        next_node, next_carry = inverse_sum(nb1.next, nb2.next)
    return Node((nb1.data + nb2.data + next_carry) % 10, next_node), (nb1.data + nb2.data + next_carry) // 10


if __name__ == '__main__':
    #n1 = create_linked_list(randint(1, 4))
    #n2 = create_linked_list(randint(1, 4))
    n1 = create_linked_list(7, upper_int=9)
    print(n1)
    n2 = create_linked_list(3, upper_int=9)
    print(n2)
    #print(sum(n1, n2))
    #print(recursive_sum(n1, n2))
    print(recursive_inverse_sum(n1, n2))