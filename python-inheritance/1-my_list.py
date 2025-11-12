#!/usr/bin/python3
"""class mylist"""
''' Module: 1-my_list'''


class MyList(list):
    """prints sorted list of class"""
    ''' Represents a MyList'''

    def print_sorted(self):
        '''prints the list, but sorted '''
        print(sorted(self))
