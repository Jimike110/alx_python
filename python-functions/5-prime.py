# Write a Python function called is_prime that takes a number as input and returns True if the number is prime, and False otherwise.

# Prototype: def is_prime(number)
# Returns True if the number is prime, and False otherwise.
# You are not allowed to import any module.

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
