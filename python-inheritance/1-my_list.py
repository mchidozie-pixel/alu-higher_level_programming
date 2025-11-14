#!/usr/bin/python3
"""MyList module"""

def _import_(name):
    module = __import__(name)
    return module


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """Prints the list but sorted (ascending sort)"""
        print(sorted(self))
