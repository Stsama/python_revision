#!/usr/bin/python3
# 2-uniq_add.py
# Albert Ezoula
def uniq_add(my_list=[]):
    """function that adds all unique integers in a list (only once for each integer)"""
    new_list = set(my_list)
    sum = 0
    for i in new_list:
        sum += i
    return (sum)
