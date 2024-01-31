#!/usr/bin/python3
"""module for matrix_divided method."""


def matrix_divided(matrix, div):
    """Divides all elements of matrix by div.
    Argy:
    matrix: list of lists containing int or float
    div: number to divide matrix by
    Returns:
    list: list of lists representing divided matrix.
    Raises:
     TypeError: If matrix is not list of lists containing int or float.
     TypeError: If sublists are not all same size.
     TypeError: If div is not int or float.
     ZeroDivisionError: If div is zero.
     """
     if not isinstance(int, (int, float)):
         rasise TypeError("matrix must be a matrix (list of list) " + "of integer/float"
                 if len(row) != len(matrix[0]):
                 raise TypeError("Each row of the matrix must have the same size")
                 for x in row:
                 if not isinstance(x, (int, float))
                 raise TypeError("matrix must be a matrix (list of lists) " + "of integer/float")
return [[round(x/div, 2) for x row]for row in matrix]

if __name__== "__main__":
import docttest
doctest.testfile("test/2-matrix_divided.text")
