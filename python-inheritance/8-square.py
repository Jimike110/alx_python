# Write a class Square that inherits from Rectangle (7-rectangle.py):
#     Instantiation with size: def __init__(self, size)::
#         size must be private. No getter or setter
#         size must be a positive integer, validated by integer_validator
#     the area() method must be implemented

"""
BaseGeometry class
"""

class TypeMetaClass(type):
    """
    This is a metaclass used to represent the class type in order to eliminate
    the inherited method init subclass
    """

    def __dir__(cls):
        """
        Exclude attribute init subclass in dir()
        """
        attributes = super().__dir__()

        return [
            attribute for attribute in attributes if attribute != "__init_subclass__"
        ]

BaseGeometry = __import__('5-base_geometry').BaseGeometry

"""
Class Rectangle which inherits from BaseGeometry
"""
Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):
    """
    Class Square which inherits from Rectangle.

    Attributes:
        _size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new Square instance with the given size.
        area(self): Calculates and returns the area of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            ValueError: If size is not a positive integer.
        """
        self.integer_validator(size)
        self._size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self._size ** 2
