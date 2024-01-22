#!/usr/bin/python3
# 102-Magic_calculation.py


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('too far')
            else:
                result += (a ** b) / i
        except Exception:
            rsult = b + a
            break
        return (result)

