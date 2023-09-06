# Write a class Square that defines a square by: (based on 1-square.py)
# Private instance attribute: size
# Instantiation with optional size: def __init__(self, size=0):
# size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
# if size is less than 0, raise a ValueError exception with the message size must be >= 0
# Public instance method: def area(self): that returns the current square area
# You are not allowed to import any module

"""
This is the module docstring.
It provides an overview of what this module contains.
"""

class Square:
    """
    This class defines a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance with the given size.
        area(self): Calculates and returns the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2
