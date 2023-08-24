# Write a Python function called fibonacci_sequence that takes a number n as input and returns a list of the first n Fibonacci numbers.

# Prototype: def fibonacci_sequence(n)
# Returns a list of the first n Fibonacci numbers.
# You are not allowed to import any module.
# Return an empty list if the it is not possible to generate the Fibonacci numbers for n

def is_prime(number):
    prime = True

    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    if number <= 1:
        return False
    elif prime:
        return True
    else:
        return False


is_prime(22)
