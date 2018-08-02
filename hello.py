#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# print('Hello, World.')
x = (1, 2, 3, 4, 5)
# x = (0, 0, 1, 0, 0)
y = (6, 7, 8, 9, 10)
z = zip(x,y)
# y = reversed(x)
# for i in y:
#     print(i)
# print(x)
# print(y)

for a, b in z:
    print(f'{a}, - {b}')
