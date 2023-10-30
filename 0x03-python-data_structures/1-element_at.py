#!/usr/bin/python3
# 1-element_at.py
# Albert Ezoula
def element_at(my_list, idx):
    """function that retrieves an element from a list like in C."""
    if idx <0 and idx > len(my_list) -1:
        return None
    return (my_list[idx])
