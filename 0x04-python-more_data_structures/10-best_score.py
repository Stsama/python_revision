#!/usr/bin/python3
# 9-multiply_by_2.py
# Albert Ezoula
def best_score(a_dictionary):
    """function that returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return (None)
    big = 0
    name = ""
    for key,value in a_dictionary.items():
        if value > big:
            big = value
            name = key
    return (name)

