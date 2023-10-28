#!/usr/bin/python3
import sys
if __name == "__main__":
    """program that prints the number of and the list of its arguments."""
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments")
    elif count == 1:
        print("1 argument")
    else:
        print("{} arguments".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, argv[i +1])) 
