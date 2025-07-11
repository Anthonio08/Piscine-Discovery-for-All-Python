#!/usr/bin/env python3
import sys
import re
param = sys.argv[1:]
lenght = len(param)

if lenght != 2:
    print("none")
else:
    parm1 = param[0]
    parm2 = param[1]
    result = re.findall(parm1, parm2)
    lenght_result = len(result)
    if lenght_result == 0:
        print("none")
    else:
        print(lenght_result)
