#!/usr/bin/env python3
import sys
param = sys.argv[1:]
lenght = len(param)
if lenght != 1:
    print("none")
else:
    print(param[0].upper())