#!/usr/bin/python3
# 1-search_replace.py


 def seach_replace(my_list, seach, replace):
     """Replace all occurences of an element by another in a new list."""
     new_list = my_list[:]
     for i in range(len(new_list)):
         if new_list[i] == seach:
             new_list[i] = replace
             return (new_list)
