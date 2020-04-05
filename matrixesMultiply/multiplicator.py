import threading
import time
m1_100 = "matrixes/m1_100_100.txt"
m1_500 = "matrixes/m1_500_500.txt"
m2_100 = "matrixes/m2_100_100.txt"
m2_500 = "matrixes/m2_500_500.txt"
m1_4 = "matrixes/m1_3_3.txt"
m2_4 = "matrixes/m2_3_3.txt"
matrix_size = 4
matrixA = [[0 for x in range(matrix_size)]
           for y in range(matrix_size)]
matrixB = [[0 for x in range(matrix_size)]
           for y in range(matrix_size)]
matrixResult = [[0 for x in range(matrix_size)]
                for y in range(matrix_size)]


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


def run():
    for i in range(matrix_size):
        for j in range(matrix_size):
            result = 0
            for k in range(matrix_size):
                result += matrixA[i][k] * matrixB[k][j]
            matrixResult[i][j] = result


if __name__ == "__main__":
    read_matrix(m1_4, matrix_size, "A")
    read_matrix(m2_4, matrix_size, "B")
    start = time.time()
    run()
    end = time.time()
    print(end - start)
