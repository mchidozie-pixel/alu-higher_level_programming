#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Returns a new list with all occurrences of 'search' replaced by 'replace'.

    Args:
        my_list (list): Original list of elements.
        search: Element to be replaced.
        replace: Element to replace with.

    Returns:
        list: New list with replaced elements.
    """
    return [replace if item == search else item for item in my_list]
