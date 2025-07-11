#!/usr/bin/env python3
origin_array =[2, 8, 9, 48, 8, 22, -12, 2]
new_array = []
greater_than_5 = []
for i in origin_array:
    new_array.append(i + 2)
print(origin_array)
for j in new_array:
    if j > 5:
        greater_than_5.append(j)
print(greater_than_5)

'''
ar = [2, 5, 6, 2]
n = [i+2 for i in ar if i>5]
print(ar)
print(n)
'''