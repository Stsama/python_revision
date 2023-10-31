#!/usr/bin/python3
# 5-number_keys.py
# Albert Ezoula
def number_keys(a_dictionary):
    """function that returns the number of keys in a dictionary."""
    num = 0;
    for k in a_dictionary.keys():
        num += 1
    return (num)
