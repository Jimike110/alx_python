# Write a function that prints a matrix of integers.
# Prototype: def print_matrix_integer(matrix=[[]]):
# Format: see example
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# You are not allowed to import any module
# You can assume that the list only contains integers
# You are not allowed to cast integers into strings
# You have to use str.format() to print integers


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end=" " if j < len(matrix[i]) - 1 else "\n")
    if len(matrix[i]) == 0:
        print(" ")