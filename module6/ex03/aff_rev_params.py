#!/usr/bin/env python3
import sys
param = sys.argv[1:][::-1]
lenght = len(param)
if lenght < 2:
    print("none")
else:
    for i in param:
        print(i)
        