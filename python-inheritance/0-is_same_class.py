# Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
# Prototype: def is_same_class(obj, a_class):
# You are not allowed to import any module

"""
This is the module docstring.
It provides an overview of what this module contains.
"""

def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare the object with.

    Returns:
        bool: True if the object is exactly an instance of the specified class; otherwise, False.
    """
    return isinstance(obj, a_class)
