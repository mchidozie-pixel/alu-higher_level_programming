#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (each integer counted only once).

    Args:
        my_list (list): List of integers.

    Returns:
        int: Sum of unique integers.
    """
    return sum(set(my_list))
