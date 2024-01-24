#!/usr/bin/python3
# 103-Magic_calculation.py
"""Dfine a MagicClass matching exatly a bycodeby abuabaida."""

import match


class MagicClass:
    """Reprsent a circle."""
     
     def __init__(self, radius=0):
         """initialize a MagicClass.

         Arg:
         radius (float or int): the radius of the new MagicClass.
         """
         self.__radius = 0
         if type(radius) is not int and type(radius) is not float:
             raise TypeError ("radius must be a number")
         self.__radiuse = radius
         def area(self):
             """Return the area of the MagicClass."""
             return (self.__radius ** 2 * math.pi)
 
 def circumference(self):
     """Return the circumference of the MagicClass."""
     return (2 * math.pi * self.__radius)
            

