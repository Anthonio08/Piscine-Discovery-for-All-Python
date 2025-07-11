#!/usr/bin/env python3
import sys
def shrink (word: str):
    x = slice(0,8)
    print(word[x])
def enlarge(word: str):
    word += "Z" * (8 - len(word))
    print(word)
param = sys.argv[1:]
lenght = len(param)
for i in param:
    if len(i) > 8:
        shrink(i)
    elif len(i) < 8:
        enlarge(i)
    elif len(i) == 8:
        print(i)