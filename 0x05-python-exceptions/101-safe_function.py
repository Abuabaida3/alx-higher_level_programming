#!/usr/bin/python3
# 101-safe_function.py

import sys


def safe_function to *args):
    """Excutes a function sacutfely.

    Args:
    fct: the function to exee.
    args: Arguments for fct.
    Returns:
    if an error occurs - none.
    otherwise - the result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (none)
