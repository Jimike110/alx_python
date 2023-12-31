# Write a class BaseGeometry (based on 3-base_geometry.py).
# Public instance method: def area(self): that raises an Exception with the message area() is not implemented
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
