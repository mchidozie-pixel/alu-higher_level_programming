#!/usr/bin/python3
"""
MyList class that inherits from list.
"""


class MyList(list):
    """
    Implements a list subclass with a method for sorted printing.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending sorted order.
        The original list remains unchanged.
        """
        print(sorted(self))
