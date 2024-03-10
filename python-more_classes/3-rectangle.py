#!/usr/bin/pyhton3
"""Define a rectangle"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """initialize a new rectangle.
        Args:
            width(int): The width of the rectanglr.
            Height(int): The height of the rectangle.
            """
        self.width = width
        self.height = height

    @property
    def width(self):
        """set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter of the rectangle"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """String representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """Representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)
