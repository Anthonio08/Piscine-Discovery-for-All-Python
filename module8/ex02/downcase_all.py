#!/usr/bin/env python3
import sys
def upcase_it(param: str):
    return param.lower()

param = sys.argv[1:]
lenght = len(param)
if lenght == 0:
    print("none")
else:
    for i in param:
        print(upcase_it(i))
