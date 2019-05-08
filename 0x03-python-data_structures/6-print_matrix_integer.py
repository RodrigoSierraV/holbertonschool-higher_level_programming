#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for y in range(len(matrix[i])):
            print("{:d}{}".format(matrix[i][y],
                  " " if y < len(matrix[i]) - 1 else ""), end="")
        print("")
