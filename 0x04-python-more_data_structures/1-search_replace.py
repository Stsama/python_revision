#!/usr/bin/python3
# 1-search_replace.py
# Ezoula Albert
def search_replace(my_list, search, replace):
    """function that replaces all occurrences of an element by another in a new list."""
    new_list = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] == 2:
            new_list[i] = replace
    return (new_list)
