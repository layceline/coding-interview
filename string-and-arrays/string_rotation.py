# Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2,
# write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a rotation
# of "erbottlewat").

def is_substring(s1: str, s2: str):
    pass

def is_a_rotation(s1: str, s2: str):
    is_rotation = False
    if len(s1) == len(s2):
        double_s1 = s1 + s1
        is_rotation = is_substring(double_s1, s2)

    return is_rotation


if __name__ == '__main__':
    input_1 = "waterbottle"
    input_2 = "erbottlewat"

    if is_a_rotation(input_1, input_2):
        print(f"{input_2} is a rotation of {input_1}")
    else:
        print(f"{input_2} isn't a substring of {input_1}")