#!/usr/bin/env python3
str_to_change = input("")
for i in str_to_change:
    if i.islower():
        print(i.upper(), end ='')
    elif i.upper():
        print(i.lower(), end='')
