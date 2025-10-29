#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides two integers and prints the result safely.

    Args:
        a (int): Numerator.
        b (int): Denominator.

    Returns:
        float or None: Result of division, or None if division fails.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
