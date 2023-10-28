#!/usr/bin/python3
import sys
if __name__ == "__main__":
     count = len(sys.argv) -1
     res = 0
     for i in range(count):
         res += int( argv[i + 1])
    print(res)
