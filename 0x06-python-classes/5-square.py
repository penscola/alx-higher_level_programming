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

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be positive")
        self.__size = value

    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
