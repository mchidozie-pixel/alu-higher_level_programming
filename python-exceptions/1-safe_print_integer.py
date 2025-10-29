#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints an integer using "{:d}".format() safely.

    Args:
        value: Any type.

    Returns:
        bool: True if value was an integer and printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
