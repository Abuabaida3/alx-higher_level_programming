#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(object, attribute, value):
    """Add a new attribute to an object if possible.
    Args:
    object (any): The object to add an atrribute to.
    attribute (str): The name of the attribute to add to object.
    value (any): The value of attribute.
    Raises:
    TypeError: If the attribute cannot be added.
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattribute(object, attribute value)
