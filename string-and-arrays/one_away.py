# There are three types of edits that can be performed on strings: insert a character, remove a character or replace a
# character. Given two strings, write a function to check if they are one edit or zero away.

# Examples
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false
from collections import Counter


def is_one_away(string1, string2):
    is_one_replace_away = False
    is_one_ins_del_away = False
    if abs(len(string1) - len(string2)) < 2:
        # in case of replace
        if len(string1) == len(string2):
            nb_diff = 0
            for char1, char2 in zip(string1, string2):
                if char1 != char2:
                    nb_diff += 1
            is_one_replace_away = nb_diff <= 1
        else:
            is_one_ins_del_away = True
            if len(string1) > len(string2):
                smaller = string2
                bigger = string1
            else:
                smaller = string1
                bigger = string2
            shift = 0
            for i in range(len(smaller)):
                if smaller[i] != bigger[i+shift]:
                    if shift == 0:
                        shift = 1
                    else:
                        is_one_ins_del_away = False
    return is_one_replace_away or is_one_ins_del_away


if __name__ == '__main__':
    input1 = "pale"
    input2 = "bake"
    print(is_one_away(input1, input2))