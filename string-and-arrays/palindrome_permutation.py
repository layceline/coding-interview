# Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or a phrase
# that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need
# to be limited to just dictionary words. You can ignore case in and non-letter characters.

# Example
# input: Tact Coa
# output: true (permutations: "taco cat", "atco cta")
from collections import Counter


def is_palindrome_permutation(input_string: str):
    input_string = input_string.lower()
    char_counter = Counter()
    for char in input_string:
        if char.isalpha():
            char_counter[char] += 1
    nb_odd_nb_occurrence = 0
    for nb_occurrence in char_counter.values():
        if nb_occurrence % 2 != 0:
            nb_odd_nb_occurrence += 1

    return (nb_odd_nb_occurrence <= 1)


if __name__ == '__main__':
    input = "Tact Coa"
    print(is_palindrome_permutation(input))
