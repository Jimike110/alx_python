# Write a class BaseGeometry (based on 4-base_geometry.py).
# Public instance method: def area(self): that raises an Exception with the message area() is not implemented
# Public instance method: def integer_validator(self, name, value): that validates value:
    # you can assume name is always a string
    # if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
    # if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
# You are not allowed to import any module

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


class BaseGeometry(metaclass=TypeMetaClass):
    """
    This is a base class
    """

    def __dir__(self):
        """
        Exclude attribute init subclass in dir()
        """
        attributes = super().__dir__()

        return [
            attribute for attribute in attributes if attribute != "__init_subclass__"
        ]

    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if value is not int:
            raise TypeError(name, "must be an integer")
        elif value <= 0:
            raise ValueError(name, "must be greater than 0")
