#!/usr/bin/python3
"""This module defines a class Square with size, position, area,
and printing.
"""


class Square:
    """A class that defines a square with private size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with optional size and position.

        Args:
            size (int): size of the square (default 0)
            position (tuple): coordinates to offset printing (default (0, 0))

        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
            TypeError: if position is not a tuple of 2 positive integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the '#' character and apply position offset."""
        if self.__size == 0:
            print()
            return

        # Print vertical offset
        for _ in range(self.__position[1]):
            print()

        # Print each line of the square
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
