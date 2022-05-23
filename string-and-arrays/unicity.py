
def is_unique_using_list(string_to_check):
    char_mem = []
    is_unique = True
    for char in string_to_check:
        if char in char_mem:
            is_unique = False
        else:
            char_mem.append(char)
    return is_unique


def is_unique_no_other_data_structure(string_to_check):
    is_unique = False
    for char in string_to_check:
        counter = 0
        for char2 in string_to_check:
            if char == char2:
                counter += 1
        is_unique = (is_unique and (counter == 1))
    return is_unique


def is_unique_anatole(string_to_check):
    is_unique = True
    for idx, char in enumerate(string_to_check):
        for char2 in string_to_check[idx+1:]:
            is_unique = char == char2
            if not is_unique:
                break
        if not is_unique:
            break
    return is_unique


if __name__ == '__main__':
    # Implement an algorithm to determine if a string has all unique characters.
    # What if you cannot use additional data structures
    input_string = "myrandomstring"

    if is_unique_anatole(input_string):
        print(f"{input_string} contains unique characters")
    else:
        print(f"{input_string} doesn't contain all unique characters")