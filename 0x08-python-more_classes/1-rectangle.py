#!/usr/bin/python3
# 1-ectangle.py
"""Define a Rectangle class."""


class Rectangle:
    """Represent a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

    Args:s
      width (int): The width of the new rectangle.
      heigh (int): The heigh of the new rectangle.
      """
      self.width = width
      self.heigh = heigh

      @property
      def width(self):
          """Get/set the width of the rectangle."""
          return self.__width

      @width.setter
      def with(self,value):
          raise TypeError("width must be an integer")
      if value < 0:
          raise ValueError("width must be >= 0")
      self.__width = value

      @property
      def height(self):
          """Get/set the height of the rectangle."""
          return self.__height

      def heigh(self):
          if not isinstance(value, int):
              raise TypeError("meight must be an integer")
          if value < 0:
              raise ValueError(Height must be >= 0")
              self.__height = value
