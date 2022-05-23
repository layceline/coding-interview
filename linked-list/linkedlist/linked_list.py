from random import randint


class Node:
    def __init__(self, data: int, next_node=None):
        self.next = next_node
        self.data = data

    def append_to_tail(self, d: int):
        end = Node(d)
        n = self
        while n.next is not None:
            n = n.next
        n.next = end

    def delete_node(self, d: int):
        if self is None:
            return None

        n = self
        if n.data == d:
            return self.next

        while n.next is not None:
            if n.next.data == d:
                n.next = n.next.next
                return self
            n = n.next
        return self

    def print(self):
        print(self.to_list())

    def __repr__(self):
        return str(self.to_list())

    def to_list(self):
        my_list = []
        if self is not None:
            n = self

            while n.next is not None:
                my_list.append(n.data)
                n = n.next
            my_list.append(n.data)
        return my_list

    @classmethod
    def from_list(cls, my_list: list):
        if my_list:
            result = Node(my_list[0])
            result.next = cls.from_list(my_list[1:])
        else:
            result = None
        return result


def create_linked_list(n, upper_int=5):
    my_list = [randint(0, upper_int) for _ in range(n)]
    return Node.from_list(my_list)