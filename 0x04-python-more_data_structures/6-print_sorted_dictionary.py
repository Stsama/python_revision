#!/usr/bin/python3
# 6-print_sorted_dictionary.py
# Albert Ezoula
def print_sorted_dictionary(a_dictionary):
    """function that prints a dictionary by ordered keys."""
    for (k, v) in sorted(a_dictionary.items()):
        print("{}: {}".format(k, v))
