#!/usr/bin/python3
# 0-square_matrix_simple.py
# Albert Ezoula
def square_matrix_simple(matrix=[]):
    """function that computes the square value of all integers of a matrix."""
    new_array = []
    for i in range(len(matrix)):
        new_array.append(list(map(lambda x : x * x, matrix[i])))
    return (new_array)
