# Given an image represented by an n x n matrix of integers, return the image rotated by 90°. Can you do it in place?


def generate_input(n):
    return [list(range(i * n, (i + 1) * n)) for i in range(n)]


def rotate_matrix_90(matrix):
    size = len(matrix)
    output = [[0] * size for _ in range(size)]
    for idxl, line in enumerate(matrix):
        output_col_index = size - (idxl + 1)
        for idx, value in enumerate(line):
            output_line = idx
            output[output_line][output_col_index] = value
    return output


def rotate_matrix_90_inplace(matrix):
    """
    Formule de rotation de 90° autour du centre d'une matrice (n+1)x(n+1)
    (x, y) -> (y, n-x) dans le sens des aiguilles d'une montre
    (x, y) -> (n-y, x) dans le sens inverse des aiguilles d'une montre
    Formule de rotation de 90° autour de 0
    (x, y) -> (y, -x) dans le sens des aiguilles d'une montre
    (x, y) -> (-y, x) dans le sens inverse des aiguilles d'une montre

    Trick: iterate only on first upper quadrant
    """
    size = len(matrix)
    # math.ceil(size / 2) <==> (size + 1) // 2
    for i in range((size+1) // 2):
        for k in range(size // 2):
            current_idx_row = k
            current_idx_col = i
            cv = matrix[current_idx_row][current_idx_col]
            for j in range(4):
                # current_value = cv
                dest_idx_col = size - (current_idx_row + 1)
                dest_idx_row = current_idx_col
                nv = matrix[dest_idx_row][dest_idx_col]
                matrix[dest_idx_row][dest_idx_col] = cv
                cv = nv
                current_idx_row = dest_idx_row
                current_idx_col = dest_idx_col


def pretty_print(matrix):
    for row in matrix:
        print(row)


if __name__ == '__main__':
    input_matrix = generate_input(6)
    pretty_print(input_matrix)
    print("\n")
    pretty_print(rotate_matrix_90(input_matrix))

    rotate_matrix_90_inplace(input_matrix)
    print("\n")
    pretty_print(input_matrix)
