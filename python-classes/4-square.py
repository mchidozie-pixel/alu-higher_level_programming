#!/usr/bin/python3
"""This module defines a class Square with a private size attribute,
getter and setter, validation, and an area method.
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
        self.size = size  # Use setter for validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): new size value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
