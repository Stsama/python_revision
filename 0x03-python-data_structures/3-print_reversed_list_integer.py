#!/usr/bin/python3
# 3-print_reversed_list_integer.py 
# Albert Ezoula
def print_reversed_list_integer(my_list=[]):
    """function that prints all integers of a list, in reverse order."""
    new = my_list[::-1]
    for i in new:
        print("{}".format(i))
