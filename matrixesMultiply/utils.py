M1_100 = "matrixes/m1_100_100.txt"
M1_500 = "matrixes/m1_500_500.txt"
M2_100 = "matrixes/m2_100_100.txt"
M2_500 = "matrixes/m2_500_500.txt"
M1_4 = "matrixes/m1_3_3.txt"
M2_4 = "matrixes/m2_3_3.txt"


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