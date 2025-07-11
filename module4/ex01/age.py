#!/usr/bin/env python3
age = input("Please tell me your age: ")
print(f"You are currently",str(age) ,"years old.")
i = 10
while i <= 30:
    int_age = int(age)
    result = i + int(age)
    print(f"in {i} years, you'll be",str(result))
    i+= 10