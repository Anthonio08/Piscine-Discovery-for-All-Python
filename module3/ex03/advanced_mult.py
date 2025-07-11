#!/usr/bin/env python3
i = 0
while i < 11:
    j = 0
    print("Table of",i,": ", end='')
    while j < 11:
        print(j*i,end= " ")
        j+= 1
    print("")
    i+=1
