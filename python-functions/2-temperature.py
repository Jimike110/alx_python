# Write a Python function called convert_to_celsius that takes a temperature in Fahrenheit as input and returns the temperature in Celsius.

# Prototype: def convert_to_celsius(fahrenheit)
# Returns the temperature in Celsius
# You are not allowed to import any module.

def convert_to_celsius(fahrenheit):
    """ (number) -> float
    Return the number of Celsius degrees equivalent to fahrenheit degrees.
    >>> convert_to_celsius(75)
    23.88888888888889
    """
    return (fahrenheit - 32.0) * 5.0 / 9.0