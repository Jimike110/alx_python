# Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
# Prototype: def is_kind_of_class(obj, a_class):
# You are not allowed to import any module

"""
This is the module docstring.
It provides an overview of what this module contains.
"""

def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance of a class that inherited from,
    the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare the object with.

    Returns:
        bool: True if the object is an instance of, or inherited from, the specified class; otherwise, False.
    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
