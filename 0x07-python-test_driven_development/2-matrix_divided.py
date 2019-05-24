#!/usr/bin/python3
"""function that divides all elements of a matrix.
   Args:
        Matrix: list of lists
        div: integer or float
"""


def matrix_divided(matrix, div):
    """Raises: TypeError if matrix is not list of lists or if lists\
       don't have the same size. Or if members aren't intergers or floats
               ZeroDivisionError if div equal to 0
       Returns: a new matrix with the result
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div is 0:
        raise ZeroDivisionError('division by zero')
    if False in [isinstance(mat, list) for mat in matrix]:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    if False in [isinstance(a, int) for b in matrix for a in b] and\
            False in [isinstance(c, float) for d in matrix for c in d]:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    if False in [len(matrix[0]) is len(j) for j in matrix]:
        raise TypeError('Each row of the matrix must have the same size')
    newmatrix = [[round(y / div, 2) for y in i] for i in matrix]
    return newmatrix
