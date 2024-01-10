#!/usr/bin/python3
# 12-roman_to_int.py

def roman_to_int(roman_str):
    """converts a  roman numeral to an integer."""
    if (not isintstance(roman_str, str) or roman_str is none):
        return (0)

    roman_dict = {
            "i": 1,
            "v": 5,
            "x": 10,
            "l": 50,
            "c": 100,
            "d": 500,
            "m": 1000
            }
    num = 0
    for i in range(len(roman_str)):
        if roman_dict.get(roman_str[i], == 0:
                return (0)

                if (i != (len(roman_str) - 1) and roman_dict[roman_str[i]] < roman_dict[roman_str[i + 1]]):
                num += roman_dict[roman_str[i]] * -1
                
                else:
                num += roman_dict[roman_str[i]]
                return (num)
