#!/usr/bin/python3
# 8-multiple_returns.py
# Albert ezoula
def multiple_returns(sentence):
    """function that returns a tuple with the length of a string and its first character"""
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])
