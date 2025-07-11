#!/usr/bin/env python3
nbr = input("Give me a number: ")
nbr_to_float = float(nbr)
if nbr_to_float != int(nbr_to_float):
    print("This number is an decimal.")
else:
    print("This number is a integer.")
