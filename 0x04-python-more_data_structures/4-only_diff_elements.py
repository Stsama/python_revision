#!/usr/bin/python3
# 4-only_diff_elements.py
# Albert Ezoula
def only_diff_elements(set_1, set_2):
    """function that returns a set of all elements present in only one set."""
    return (set_1 ^ set_2)
