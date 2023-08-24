# Write a Python function called fibonacci_sequence that takes a number n as input and returns a list of the first n Fibonacci numbers.

# Prototype: def fibonacci_sequence(n)
# Returns a list of the first n Fibonacci numbers.
# You are not allowed to import any module.
# Return an empty list if the it is not possible to generate the Fibonacci numbers for n

def fibonacci_sequence(n):
    result = []
    num = 0
    if n == 1:
        result.append(0)
        return result
    elif n <= 0:
        return result
    result.append(num)
    result.append(1)
    for i in range(2, n):
        num = result[i-2] + result[i-1]
        result.append(num)
    return result