#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Hər bir satırdakı integer-ləri str.format ilə çap edirik
        print(" ".join("{:d}".format(num) for num in row))
