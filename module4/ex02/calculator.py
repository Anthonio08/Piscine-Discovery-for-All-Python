#!/usr/bin/env python3
nbr1 = int(input("Give me the first number: "))
nbr2 = int(input("Give me the second number: "))
print("Thank you!")
print(f"{nbr1} + {nbr2} = {nbr1 + nbr2}")
print(f"{nbr1} - {nbr2} = {nbr1 - nbr2}")
if nbr1 == 0 or nbr2 == 0:
    print("error")
else:    
    print(f"{nbr1} / {nbr2} = {int(nbr1 / nbr2)}")
print(f"{nbr1} * {nbr2} = {nbr1 * nbr2}")