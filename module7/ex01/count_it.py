#!/usr/bin/env python3
import sys
param = sys.argv[1:]
lenght = len(param)
if lenght == 0:
    print("none")
else:
    print(f"parameters:{lenght}")
    for i in param:
        arg_lenght = len(i)
        print(f"{i}: {arg_lenght}")