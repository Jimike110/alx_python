# Write a class Square that inherits from Rectangle (7-rectangle.py):
#     Instantiation with size: def __init__(self, size)::
#         size must be private. No getter or setter
#         size must be a positive integer, validated by integer_validator
#     the area() method must be implemented

"""
BaseGeometry class
"""

TypeMetaClass = __import__('7-rectangle').TypeMetaClass

BaseGeometry = __import__('5-base_geometry').BaseGeometry

Rectangle = __import__('7-rectangle.py').Rectangle

class Square(Rectangle):
    def __init__(self, size):
        self._size = size
        self.integer_validator(self._size)
    def area(self):
        return self._size ** 2