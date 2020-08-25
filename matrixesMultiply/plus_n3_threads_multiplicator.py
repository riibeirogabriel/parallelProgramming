import threading
from concurrent.futures import ThreadPoolExecutor, wait
import time
import utils as utils


MATRIX_SIZE = 4

plus_thread_pool = ThreadPoolExecutor(max_workers=20)
threads = []
matrix_a = utils.generate_matrix(MATRIX_SIZE)
matrix_b = utils.generate_matrix(MATRIX_SIZE)
matrix_result = utils.generate_matrix(MATRIX_SIZE)
matrix_aux = utils.generate_aux_matrix(MATRIX_SIZE)


def n2_threads(id, line, column, iterator):
    global matrix_result, matrix_a, matrix_b
    matrix_aux[id][iterator] = matrix_a[line][iterator] * \
        matrix_b[iterator][column]


def plus_threads(index):
    global matrix_result, matrix_a, matrix_b
    result = list()
    aux = list()
    num_threads_plus = int(MATRIX_SIZE / 2)

    for i in range(MATRIX_SIZE):
        result.append(matrix_aux[index][i])

    while(len(result) > 1):
        for j in range(num_threads_plus):
            threads.append(plus_thread_pool.submit(plus(aux, result, j)))

        result = aux.copy()
        aux.clear()
        num_threads_plus = int(num_threads_plus / 2)

    line = int(index / MATRIX_SIZE)
    column = int(index % MATRIX_SIZE)
    matrix_result[line][column] = result[0]


def plus(aux, array, indice):
    aux.append(array[indice * 2] + array[(indice * 2) + 1])


def run_threads():
    global threads
    count = 0

    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            for k in range(MATRIX_SIZE):
                threads.append(
                    plus_thread_pool.submit(
                        n2_threads(
                            count, i, j, k)))
            count += 1

    wait(threads)
    threads.clear()

    for i in range(MATRIX_SIZE * MATRIX_SIZE):
        threads.append(plus_thread_pool.submit(plus_threads(i)))

    wait(threads)
    threads.clear()


if __name__ == "__main__":
    matrix_a = utils.read_matrix(utils.MATRIX_A_4_LINES)
    matrix_b = utils.read_matrix(utils.MATRIX_B_4_LINES)

    start = time.time()
    run_threads()
    end = time.time()

    print(end - start)
    print(matrix_result)
