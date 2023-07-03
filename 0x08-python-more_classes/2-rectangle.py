#!/usr/bin/python3
"""Module that defines a rectangle"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2
    
    def __str__(self):
        """Return string representation of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)
