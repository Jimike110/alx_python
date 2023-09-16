# Write an empty class BaseGeometry.
# You are not allowed to import any module

"""
Module documentation
"""

class BaseGeometry:
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
