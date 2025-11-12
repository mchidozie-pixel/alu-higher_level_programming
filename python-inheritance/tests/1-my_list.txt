#!/usr/bin/python3
"""
Module 1-my_list
Contains the MyList class, which inherits from the built-in list class.
"""

class MyList(list):
    """
    A class MyList that inherits from list.

    It provides a public instance method:
        - def print_sorted(self): prints the list, but sorted (ascending sort).
    Assumes all elements are integers.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.
        This method does not modify the original list object.
        """
        # The sorted() function returns a new sorted list from the items in self (the current MyList instance)
        print(sorted(self))
