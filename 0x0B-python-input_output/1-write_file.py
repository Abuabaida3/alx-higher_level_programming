#!/usr/bin/pyth3
# 1-number_of_line.py
"""Define a text file line-counting function."""


def number_of_lines(filename=""):
    """Return the number of lines in a text file."""
    lines = 0
    with open(filename, as f:
            for line in f:
            lines += 1
            return lines
