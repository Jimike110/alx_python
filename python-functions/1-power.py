# Write a function that computes a to the power of b and return the value.

# Prototype: def pow(a, b):
# Returns the value of a ^ b
# You are not allowed to import any module

def pow(a, b):
    # Base case: Any number raised to the power of 0 is 1
    if b == 0:
        return 1
    
    # Base case: Any number raised to the power of 1 is the number itself
    if b == 1:
        return a
    
    # For negative exponents, compute the reciprocal of the result
    if b < 0:
        return 1 / pow(a, -b)
    
    # For positive exponents greater than 1, use recursion to compute the result
    return a * pow(a, b - 1)