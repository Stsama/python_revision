#!/usr/bin/python3
# 6-print_comb3.py
# Created by Albert Ezoula
for i in range(9):
    for j in range(i+1, 10):
        if i == 8 and j == 9:
            print('{}{}'.format(i, j))
        else:
            print('{}{}'.format(i,j), end= ", ")
