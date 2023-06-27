#!/usr/bin/python3
"""Module defines a class Square"""


class Square:
    """Class defines a square"""
    def __init__(self, size=0):
        """Initializes the data"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be positive")
        self.__size = size
