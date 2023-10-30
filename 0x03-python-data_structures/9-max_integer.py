#!/usr/bin/python3
# 9-max_integer.py
# Albert Ezoula
def max_integer(my_list=[]):
    """ function that finds the biggest integer of a list."""
    if my_list == 0:
        return None
    
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return (max)
