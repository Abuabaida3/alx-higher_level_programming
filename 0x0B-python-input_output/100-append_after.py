#!/usr/bin/python3
# 100-append_after.py
"""Define a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.
    Args:
       filename (str): The name of the file.
       seach_string (str): The string to seach for within the file.
       new_string to insert.
       """
       text = ""
       with open(filename) as r:
           for line in r:
               text += line
               if seach_string in line:
                   text += new_string 
                   wiht open(filename, "w") as w:
                       w.write(text)
