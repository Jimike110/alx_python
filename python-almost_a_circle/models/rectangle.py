# Write the class Rectangle that inherits from Base:

# In the file models/rectangle.py
# Class Rectangle inherits from Base
# Private instance attributes, each with its own public getter and setter:
# __width -> width
# __height -> height
# __x -> x
# __y -> y
# Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
# Call the super class with id - this super call with use the logic of the __init__ of the Base class
# Assign each argument width, height, x and y to the right attribute
# Why private attributes with getter/setter? Why not directly public attribute?

# Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. 
# So after, in your class you can “trust” these attributes.

# models/rectangle.py

"""
Module: rectangle

This module defines the Rectangle class, which inherits from the Base class.
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

class Rectangle(Base):
    """
    Class Rectangle inherits from Base.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x-coordinate of the rectangle.
        __y (int): The y-coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): The id for the instance. If provided, it will be passed to the Base class constructor.

        Note:
            Width and height must be positive integers.
        """
        super().__init__(id)
        self.__width = None
        self._set_width(width)  # Setters are used for validation purposes only!
        self.__height = None
        self._set_height(height)
        self.__x = None
        self._set_x(x)
        self.__y = None
        self._set_y(y)

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def _set_width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): The value to set as the width.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def _set_height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): The value to set as the height.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x-coordinate attribute.

        Returns:
            int: The x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def _set_x(self, value):
        """
        Setter for the x-coordinate attribute.

        Args:
            value (int): The value to set as the x-coordinate.
        """
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y-coordinate attribute.

        Returns:
            int: The y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def _set_y(self, value):
        """
        Setter for the y-coordinate attribute.

        Args:
            value (int): The value to set as the y-coordinate.
        """
        self.__y = value
