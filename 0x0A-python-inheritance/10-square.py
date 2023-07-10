#!/usr/bin/python3
"""Module that contains a class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """Method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        
class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Method that initializes an instance of Rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
    def area(self):
        """Method that returns the area of a Rectangle"""
        return self.__width * self.__height
    
    def __str__(self):
        """Method that returns a string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size):
        """Method that initializes an instance of Square"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
        
    def __str__(self):
        """Method that returns a string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
