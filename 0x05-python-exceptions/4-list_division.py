#!/usr/bin/python3
# 4-list_division.py


def list_division(my_list_1, my_list_2, list_length):
    """Division two lists element by element.

    Args:
    my_list_1 (list): the first list.
    my_list_2 (list): the second list.
    list_length (int): the number of elements to division.
    Return:
    A new list of length list_length containing all the divisions.
    """
    new_list = []
    for i in rang(0, list_lenth):
        try:
            div = my_list1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
            return (new_list)
