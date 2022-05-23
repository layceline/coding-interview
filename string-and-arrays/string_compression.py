# Implement a method to perform basic string compression using the counts of repeated characters. For example, the
# string 'aabcccccaaa' would become 'a2b1c5a3'. If the compressed string would not become smaller than the original
# string, your method should return the original string. You can assume that the string has only upper and lower
# case a to z.
from collections import Counter


def compress(string_to_compress):
    output_list = []
    current_counter = 0
    current_char = ""
    for char in string_to_compress:
        if char == current_char:
            current_counter += 1
        else:
            current_char = char
            output_list.append(str(current_counter))
            output_list.append(current_char)
            current_counter = 1

    output_list.append(str(current_counter))
    output = "".join(output_list[1:])
    if len(string_to_compress) < len(output):
        output = string_to_compress
    return output


if __name__ == '__main__':
    input = 'aabcccccaaa'
    print(compress(input))
