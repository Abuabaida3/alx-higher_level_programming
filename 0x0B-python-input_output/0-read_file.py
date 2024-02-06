#!/usr/bin/python3
# 0-read_file.py
"""Define a text file-reading function."""


def read_file(filename=""):
    """print the contents of a UTF8 text file to stdout."""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
