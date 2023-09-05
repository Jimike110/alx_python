# Write a class Square that defines a square by:
# Private instance attribute: size
# Instantiation with size (no type/value verification)
# You are not allowed to import any module

class Square:
    __size = None

    def __init__(self, __size):
        size = __size