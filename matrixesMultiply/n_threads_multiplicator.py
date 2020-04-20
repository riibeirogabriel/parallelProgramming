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


class nThreads(threading.Thread):
    line = 0
    def __init__(self, threadID, name, line):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.line = line

    def run(self):
        global matrixResult, matrixA, matrixB
        for i in range(matrix_size):
            result = 0
            for j in range(matrix_size):
                result += matrixA[self.line][j] * matrixB[j][i]
            matrixResult[self.line][i] = result
            
def read_matrix(file_name,size,typeMatrix):
    global matrixA,matrixB
    file = open(file_name,"r")
    Matrix = list() 
    file.read(1)
    for i in file:
        Matrix.append(list(map(int,i.split())))
        
    if(typeMatrix == "A"):
        matrixA = Matrix
    else:
        matrixB = Matrix

def run_threads():
    threads = list()
    for i in range(matrix_size):
        threads.append(nThreads(i,"Thread " + str(i),i))
        threads[i].start()
    
    for thread in threads:
        thread.join()
        


if __name__ == "__main__":
   
    read_matrix(m1_4,matrix_size,"A")
    read_matrix(m2_4,matrix_size,"B")
    start = time.time()
    run_threads()
    end = time.time()
    print(end - start)
    print(matrixResult)
