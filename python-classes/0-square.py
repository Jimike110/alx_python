# Write a class Square that defines a square by:
# Private instance attribute: size
# Instantiation with size (no type/value verification)
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
        __init__(self, size): Initializes a new Square instance with the given size.
        area(self): Calculates and returns the area of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
