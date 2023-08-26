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
            # Print the element without moving to the next line
            print("{:d}".format(matrix[i][j]), end=" ")
        print()  # Move to the next line after each row


# Define the matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Call the function with the defined matrix
print_matrix_integer(matrix)
