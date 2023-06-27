#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """Square class with a private attribute -
    size.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data."""
        self.size = size
        self.position = position

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
    
    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position
    
    @position.setter
    def position(self, value):
        """Sets the position of the square."""
        if type(value) is not tuple or len(value) != 2 or \
        type(value[0]) is not int or value[0] < 0 or \
        type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
