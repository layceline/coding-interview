# Write an algorithm such that if an element in an M x N matrix is 0, its entire row and column are set to 0.
import random


def generate_matrix(nb_rows, nb_cols):
    output = []
    for i in range(nb_rows):
        row = []
        for j in range(nb_cols):
            row.append(random.randint(0, 10))
        output.append(row)
    return output


def pretty_print(matrix):
    for line in matrix:
        print(line)


def set_zero_matrix(matrix):
    row_size = len(matrix)
    col_size = len(matrix[0])
    zero_row_index = set()
    zero_col_index = set()
    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            if value == 0:
                zero_row_index.add(row_index)
                zero_col_index.add(col_index)

    for row_index in zero_row_index:
        for i in range(col_size):
            matrix[row_index][i] = 0

    for col_index in zero_col_index:
        for i in range(row_size):
            matrix[i][col_index] = 0


if __name__ == '__main__':
    input_matrix = generate_matrix(3, 4)
    pretty_print(input_matrix)
    print("\n")
    set_zero_matrix(input_matrix)
    pretty_print(input_matrix)
