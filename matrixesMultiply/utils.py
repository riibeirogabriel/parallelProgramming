MATRIX_A_4_LINES = "matrixes/matrix_a_4_lines.txt"
MATRIX_B_4_LINES = "matrixes/matrix_b_4_lines.txt"

MATRIX_A_100_LINES = "matrixes/matrix_a_100_lines.txt"
MATRIX_B_100_LINES = "matrixes/matrix_b_100_lines.txt"

MATRIX_A_500_LINES = "matrixes/matrix_a_500_lines.txt"
MATRIX_B_500_LINES = "matrixes/matrix_b_500_lines.txt"


def read_matrix(file_name):
    file = open(file_name, "r", encoding="utf-8")
    matrix = list()
    for line in file.readlines():
        matrix.append(list(map(int, line.split())))
    return matrix


def generate_matrix(size):
    return [[0 for y in range(size)]
            for x in range(size)]


def generate_aux_matrix(size):
    return [[0 for x in range(size)]
            for y in range(size * size)]