#!/usr/bin/python3
# 8-simple_delete.py
# Albert Ezoula
def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary:
        return a_dictionary
    del a_dictionary[key]
    return a_dictionary
