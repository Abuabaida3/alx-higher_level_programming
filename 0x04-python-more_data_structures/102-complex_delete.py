#!/usr/bin/python3
# 102-complex_delete.py


def complex_delete(a_dictionary, value):
    """delete keys with a specific value in a dictionary."""
    while value in a_dictionary.value():
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                break
            return (a_dictionary)
