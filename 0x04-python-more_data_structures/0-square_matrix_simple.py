#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = [[matrix[i][y]**2 for y in range(len(matrix[i]))]
               for i in range(len(matrix))]
    return squares
