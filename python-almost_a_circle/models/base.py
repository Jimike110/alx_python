# Write the first class Base:

# Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package

# Create a file named models/base.py:

# Class Base:
# private class attribute __nb_objects = 0
# class constructor: def __init__(self, id=None)::
# if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
# otherwise, increment __nb_objects and assign the new value to the public instance attribute id
# This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)


"""
Module: base

This module defines the Base class, which serves as the base class for other classes in the project.
"""

class Base:
    """
    Class Base serves as the base class for other classes in the project.

    Attributes:
        __nb_objects (int): A private class attribute to manage the id attribute in all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): The id for the instance. If provided, it will be assigned to the id attribute.
                If not provided, the __nb_objects counter will be incremented and assigned as the id.

        Note:
            You can assume that id is an integer.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
