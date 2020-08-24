import threading
import time
import utils as utils

MATRIX_SIZE = 4

threads = []
matrix_a = utils.generate_matrix(MATRIX_SIZE)
matrix_b = utils.generate_matrix(MATRIX_SIZE)
matrix_result = utils.generate_matrix(MATRIX_SIZE)
matrix_aux = utils.generate_aux_matrix(MATRIX_SIZE)


class n_threads(threading.Thread):
    line = 0

    def __init__(self, thread_id, name, line):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.line = line

    def run(self):
        global matrix_result, matrix_a, matrix_b
        for i in range(MATRIX_SIZE):
            result = 0

            for j in range(MATRIX_SIZE):
                result += matrix_a[self.line][j] * matrix_b[j][i]

            matrix_result[self.line][i] = result


def run_threads():
    threads = list()
    for i in range(MATRIX_SIZE):
        threads.append(n_threads(i, "Thread " + str(i), i))
        threads[i].start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    matrix_a = utils.read_matrix(utils.M1_4)
    matrix_b = utils.read_matrix(utils.M2_4)

    start = time.time()
    run_threads()
    end = time.time()

    print(end - start)
    print(matrix_result)
