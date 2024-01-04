#!/usr/bin/python3
# 100-my_calculatator.py

if __name__ == "__main__":
    """handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) -1 != 3:
        print("usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

ops = {"+": add, "_": sub, "*": mul, "/": div}
if sys.argv[2] not in list(ops.keys())
print("unknown opertor. available operators: +, -, *nand /")
sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])
print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
