#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for numbers in matrix:
        for index in range(len(numbers)):
            print("{:d}".format(numbers[index]), end="")
            if index < len(numbers) - 1:
                print(" ", end="")
        print()
