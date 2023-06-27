#!/usr/bin/python3
"""Module defines a class Square"""


class Square:
    """Class defines a square"""
    def __init__(self, size=0):
        """Initializes the data"""
        self.size = size

    @property
    def size(self):
        """Getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be positive")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __lt__(self, other):
        """Less than"""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Equal"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal"""
        return self.area() >= other.area()
