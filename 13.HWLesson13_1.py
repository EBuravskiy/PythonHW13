def printmatrix(matrix):
    for i in matrix:
        print(i)

def summatrix(rows, cols, matrix_a, matrix_b):
    matrix_result = [[0 for i in range(cols)]for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            matrix_result[i][j] = matrix_a[i][j]+matrix_b[i][j]
    return matrix_result
from random import randint
rows = int(input("Enter the number of rows in the matrix: "))
cols = int(input("Enter the number of collumns in the matrix: "))
matrix_a = [[(randint(-200, 200)) for i in range(cols)]for i in range(rows)]
print("Created matrix A with random numbers: ")
printmatrix(matrix_a)
print('')
matrix_b = [[(randint(-200, 200)) for i in range(cols)]for i in range(rows)]
print("Created matrix B with random numbers: ")
printmatrix(matrix_b)
print('')
matrix_result = summatrix(rows, cols, matrix_a, matrix_b)
print("Result of sum of matrix: ")
printmatrix(matrix_result)
