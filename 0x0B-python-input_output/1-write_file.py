#!/usr/bin/python3


def number_of_lines(filename=""):
    with open(filename, "r", encodin="UTF-8") as f:
        return len(list(f))
