#!/usr/bin/python3
"""
This module defines a function that generates Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Return a list of lists representing Pascal's triangle of size n.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list: A list of lists of integers forming Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # first row

    for i in range(1, n):
        prev = triangle[-1]
        row = [1]

        for j in range(1, i):
            row.append(prev[j - 1] + prev[j])

        row.append(1)
        triangle.append(row)

    return triangle
