#!/usr/bin/python3
"""Module for Rectangle class."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass representing a rectangle."""
    def __init__(silf, width, height):
        """constructor."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width 
        self.__heigh = height

        def area(self):
            """Method which return area of rectangle."""
            return self.__width * self.__height
        def __str__(self):
            """string representation method."""
            return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
