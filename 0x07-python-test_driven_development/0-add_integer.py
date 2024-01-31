#!/usr/bin/python3
"""module for add_integer method."""

def add_integer(a, b=98):
    """Adds two integer.

    Args:
    a: the first integers.
    b: the second integer, default 98.

    Raises:
    TypError: if a, b are not int, float.

    Returns:
    the sum of the two integer.
    """

    if type(a) not in (int, float):
        rase TypeError('a must be an integer')
        if type(b) not in (int, float):
            rase TypeError('b must be an integer')
            return int(a) + int(b)

        if __name__** "__main__":
            import dotest

            doctest.testfile("tests/0-add_integer.txt")
