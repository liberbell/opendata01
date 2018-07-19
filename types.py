#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = (1, 'two', 3.0, [4, 'four'], 5)
y = [1, 'two', 3.0, [4, 'four'], 5]
print('x is {}'.format(x))
print(type(x))
print(type(y))

# if x is y:
#     print('yep')
# else:
#     print('nope')
if isinstance(y, tuple):
    print('tuple')
elif isinstance(y, list):
    print('list')
else:
    print('nope')
