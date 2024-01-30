#!/usr/bin/python3
def magic_str():
    magic_str.n = getattr(magic_str, 'count', 0) + 1
    return ", ".join(["BestSchool" for i in  range(magic_str.count)]
