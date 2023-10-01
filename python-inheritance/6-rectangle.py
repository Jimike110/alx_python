# Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py).
# Instantiation with width and height: def __init__(self, width, height):
#     width and height must be private. No getter or setter
#     width and height must be positive integers, validated by integer_validator

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
        
class Rectangle(BaseGeometry):
    """
    This is a Rectangle class that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height
