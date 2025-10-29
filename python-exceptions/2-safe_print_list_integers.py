#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x integers of a list, skipping non-integers.

    Args:
        my_list (list): List with mixed types.
        x (int): Number of elements to access in the list.

    Returns:
        int: Number of integers actually printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print()
    return count
