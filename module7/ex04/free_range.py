#!/usr/bin/env python3
import sys
param = sys.argv[1:]
lenght = len(param)
if lenght != 2:
    print("none")
else:
    param1 = int(param[0])
    param2 = int(param[1])
    array = []
    for i in range(param1, param2 + 1):
        array.append(i)
    print(array)