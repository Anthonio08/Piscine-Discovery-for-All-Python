#!/usr/bin/env python3
import sys
param = sys.argv[1:]
lenght = len(param)
if lenght != 1:
    print("none")
else:
    input_word = input("What was the parameter ? ")
    if param[0] == input_word:
        print("Good job!")
    else:
        print("Nope, sorry...")