#!/usr/bin/python3
"""This module defines a class Square with a private size attribute,
validation, and an area method.
"""


class Square:
    """A class that defines a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize a square with an optional size.

        Args:
            size (int): size of the square (default 0)

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
