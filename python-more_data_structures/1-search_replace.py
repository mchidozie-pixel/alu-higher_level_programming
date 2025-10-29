#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Returns a new list where all occurrences of 'search' are replaced with 'replace'."""
    # Create a new list with replaced elements
    new_list = [replace if item == search else item for item in my_list]
