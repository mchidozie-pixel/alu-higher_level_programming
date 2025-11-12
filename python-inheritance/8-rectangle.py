#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.

The Rectangle class represents a rectangle shape with a width and a height.
Both attributes are private and validated to ensure they are positive integers.

Classes:
    Rectangle(BaseGeometry): Represents a rectangle with width and height.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).

    Methods:
        __init__(self, width, height): Initializes a Rectangle with width and height.
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with width and height.

        Both width and height are validated to be positive integers
        using the integer_validator method from BaseGeometry.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height <= 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
