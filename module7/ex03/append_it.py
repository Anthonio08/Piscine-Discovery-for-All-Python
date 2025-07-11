#!/usr/bin/env python3
import sys
param = sys.argv[1:]
lenght = len(param)
if lenght == 0:
    print("none")
else:
    for i in param:
        if i.find("ism") == -1:
            i += "ism"
            print(i)
   
