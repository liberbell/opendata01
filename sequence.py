#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = list(range(5))
x[2] = 42
for i in x:
    print('i is {}'.format(i))
