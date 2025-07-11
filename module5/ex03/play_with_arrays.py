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
array_to_set = set(greater_than_5)
print(array_to_set)
