#!/usr/bin/python3



def read_file(filename="UTF-8"):
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="UTF-8")
