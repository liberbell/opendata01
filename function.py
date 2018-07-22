#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = [5]
    y = x
    y[0] = 3
    print(id(x))
    print(id(y))
    print(x)
    print(y)
    # kitten(x)
    # print(f"in main: x is {x}")
    # x = kitten(5, 6, 7)
    # print(x)

def kitten(a):
    # print(id(a))
    a = 3
    print(id(a))
    print('Meow.')
    print(a)

if __name__ == '__main__': main()
