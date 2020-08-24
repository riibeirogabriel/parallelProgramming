import threading
import time
import utils as utils

MATRIX_SIZE = 4

threads = []
matrix_a = utils.generate_matrix(MATRIX_SIZE)
matrix_b = utils.generate_matrix(MATRIX_SIZE)
matrix_result = utils.generate_matrix(MATRIX_SIZE)
matrix_aux = utils.generate_aux_matrix(MATRIX_SIZE)


def run():
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            result = 0

            for k in range(MATRIX_SIZE):
                result += matrix_a[i][k] * matrix_b[k][j]

            matrix_result[i][j] = result


if __name__ == "__main__":
    matrix_a = utils.read_matrix(utils.MATRIX_A_4_LINES)
    matrix_b = utils.read_matrix(utils.MATRIX_B_4_LINES)

    start = time.time()
    run()
    end = time.time()

    print(end - start)
    print(matrix_result)
