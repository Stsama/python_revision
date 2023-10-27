#!/usr/bin/python3
# 9-print_last_digit.py
# Created by Albert Ezoula

def print_last_digit(number):
    """a function that prints the last digit of a number."""
    last = abs(number) % 10
    print(last, end='')
    return last

