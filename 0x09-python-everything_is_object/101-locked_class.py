#!/usr/bin/python3
# 101-locked_class.py
"""Dfine a locked class."""


class lockedClass:
    """
    prevent the user from instantiating new lockedClass attributes
    for anything but attributes called 'first_name'.
    """
    __slots__ = ["first_name"]
