#!/usr/bin/python3
# 4-new_in_list.py
# Albert Ezoula
def new_in_list(my_list, idx, element):
    """function that replaces an element in a list at a specific position without modifying the original list"""
    if idx < 0 and idx >= len(my_list):
        return my_list
    new = my_list.copy()
    new[idx] = element
    return (new)
