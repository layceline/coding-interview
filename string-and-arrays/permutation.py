import sys
from collections import Counter


def is_permutation(input_1, input_2):
    is_permutation = False

    if len(input_1) == len(input_2):
        input_1_unique_chars = Counter()
        for char in input_1:
            input_1_unique_chars[char] += 1
        for char in input_2:
            input_1_unique_chars[char] -= 1

        is_permutation = (max(input_1_unique_chars.values()) == 0 and min(input_1_unique_chars.values()) == 0)

    return is_permutation


if __name__ == '__main__':
    # Given two strings, write a method to decide if on is a permutation of the other
    my_string_1 = 'toto'
    my_string_2 = 'oott'
    if is_permutation(my_string_1, my_string_2):
        print(f"{my_string_1} is a permutation of {my_string_2}")
    else:
        print(f"{my_string_1} isn't a permutation of {my_string_2}")