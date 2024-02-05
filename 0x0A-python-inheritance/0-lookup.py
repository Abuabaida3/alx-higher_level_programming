#!/usr/bin/python3
"""module for lookup method."""


def lookup(obj):
    """loks up object attributes and methods.
    Args:
    obj (object): the object to list.

    Returns:
    list: the of attributes.
    """
    return dir(obj)
