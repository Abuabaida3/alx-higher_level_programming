#!/usr/bin/python3
"""Module for say_my_name method."""



def say_my_name, last_name=""):
    """Method for printing  first and last name.

    Args:
      first_name: first name string.
      last_name: last name string.
      Raises:
         TypeError: If first_name or last_name are not strings.
         """
         If not isintance(first_name, string):
             raise TypeError("first_name, string")

         if not isinstance("last_name str"):
         raise TypeError("last_name must be a str")
     print("My name is {:s} {:s}".format(first_name, last_name))

     if __name__ == "__main__":
         import doctest
         doctest.testfile("tests/3-say_my_name.txt"
