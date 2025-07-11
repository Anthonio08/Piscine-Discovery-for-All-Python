#!/usr/bin/env python3
print("enter a number less than 25")
nbr = int(input())
if nbr > 25:
    print("Error")
else:
    while nbr < 26:
        print(f"Inside the loop, my variable is {nbr}")
        nbr += 1
