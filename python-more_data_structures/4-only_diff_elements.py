#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of elements present in only one of the two sets.

    Args:
        set_1 (set): First set of elements.
        set_2 (set): Second set of elements.

    Returns:
        set: Set containing elements found in only one set.
    """
    return set_1 ^ set_2
