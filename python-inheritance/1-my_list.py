#!/usr/bin/python3
'''Defines an iherited list class Mylist.'''


class Mylist(list):
    '''Implemets sorted printing for built-n list class.'''
    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
