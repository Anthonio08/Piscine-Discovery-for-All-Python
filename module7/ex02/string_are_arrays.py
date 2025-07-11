#!/usr/bin/env python3
import sys
import re
param = sys.argv[1:]
lenght = len(param)
if lenght == 1:
    search_z = re.findall("z", param[0])
    lenght_search_z = len(search_z)
    if lenght_search_z == 0:
        print("none")
    else:
        for i in param[0]:
            if i == "z":
                print(i,end='')
else:
    print("none")                