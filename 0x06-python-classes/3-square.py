#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """Square class with a private attribute -
    size.
    """
    def __init__(self, size=0):
        """Initializes the data."""
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
