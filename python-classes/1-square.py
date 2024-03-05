#!/usr/bin/python3
"""Define a class Square"""


class Square:
    def __init__(self, size):
        """init size"""
         if not isinstance(size, int):
             raise TypeError("size must be an integer")
         elif size < 0:
             raise ValueError("size must be >= o")
         self.__size = size
