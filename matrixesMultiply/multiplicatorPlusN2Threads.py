import threading
from concurrent.futures import ThreadPoolExecutor, wait
import time

m1_100 = "matrixes/m1_100_100.txt"
m1_500 = "matrixes/m1_500_500.txt"
m2_100 = "matrixes/m2_100_100.txt"
m2_500 = "matrixes/m2_500_500.txt"
m1_4 = "matrixes/m1_3_3.txt"
m2_4 = "matrixes/m2_3_3.txt"
matrix_size = 4

plusThreadsPool = ThreadPoolExecutor(max_workers=250)
threads = []
matrixA = [[0 for x in range(matrix_size)]
           for y in range(matrix_size)]
matrixB = [[0 for x in range(matrix_size)]
           for y in range(matrix_size)]
matrixResult = [[0 for x in range(matrix_size)]
                for y in range(matrix_size)]
matrixAux = [[0 for x in range(matrix_size)]
             for y in range(matrix_size * matrix_size)]


def n2Threads(id, line, collumn, iterator):
    global matrixResult, matrixA, matrixB
    matrixAux[id][iterator] = matrixA[line][iterator] * \
        matrixB[iterator][collumn]


def plusThreads(index):
    global matrixResult, matrixA, matrixB
    result = list()
    aux = list()
    numThreadsPlus = int(matrix_size / 2)

    for i in range(matrix_size):
        result.append(matrixAux[index][i])
    while(len(result) > 1):
        for j in range(numThreadsPlus):
            threads.append(plusThreadsPool.submit(plus(aux, result, j)))
        result = aux.copy()
        aux.clear()
        numThreadsPlus = int(numThreadsPlus / 2)

    line = int(index / matrix_size)
    collumn = int(index % matrix_size)
    matrixResult[line][collumn] = result[0]


def plus(aux, array, indice):
    aux.append(array[indice * 2] + array[(indice * 2) + 1])


def read_matrix(file_name, size, typeMatrix):
    global matrixA, matrixB
    file = open(file_name, "r")
    Matrix = list()
    file.read(1)
    for i in file:
        Matrix.append(list(map(int, i.split())))
    if(typeMatrix == "A"):
        matrixA = Matrix
    else:
        matrixB = Matrix


def run_threads():
    global threads
    count = 0
    for i in range(matrix_size):
        for j in range(matrix_size):
            for k in range(matrix_size):
                threads.append(plusThreadsPool.submit(n2Threads(count, i, j, k)))
            count += 1
    wait(threads)
    threads.clear()
    for i in range(matrix_size * matrix_size):
        threads.append(plusThreadsPool.submit(plusThreads(i)))
    wait(threads)
    threads.clear()


if __name__ == "__main__":
    read_matrix(m1_4, matrix_size, "A")
    read_matrix(m2_4, matrix_size, "B")
    start = time.time()
    run_threads()
    end = time.time()
    print(end - start)
