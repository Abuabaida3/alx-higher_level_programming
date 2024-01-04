#!/usr/bin/python3
# 102-magic_calculation.py
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a > b:
        return a + b
    elif a < b:
        return a - b
    else:
        return a * b

