#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix."""
    # Create a new matrix by squaring each element
    new_matrix = [[value ** 2 for value in row] for row in matrix]
    return new_matrix
