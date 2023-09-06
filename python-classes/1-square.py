# Write a class Square that defines a square by: (based on 0-square.py)
# Private instance attribute: size
# Instantiation with optional size: def __init__(self, size=0):
# size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
# if size is less than 0, raise a ValueError exception with the message size must be >= 0
# You are not allowed to import any module

"""
This is the module documentation.
"""

class Square:
    """
    Class documentation
    """
    def __init__(self, size=0):
        __size = size

        try:
            int(size)
        except TypeError:
            print("size must be an integer")
        if size < 0:
            raise ValueError(print("size must be >= 0"))