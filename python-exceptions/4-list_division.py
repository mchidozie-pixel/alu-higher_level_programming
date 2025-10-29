#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element two lists and handles exceptions.

    Args:
        my_list_1 (list): First list of elements.
        my_list_2 (list): Second list of elements.
        list_length (int): Number of elements to process.

    Returns:
        list: List of division results (float), 0 on errors.
    """
    result = []
    for i in range(list_length):
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
