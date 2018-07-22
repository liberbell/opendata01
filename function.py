#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = kitten(5, 6, 7)
    # print(x)

def kitten(a, b, c = 0):
    print('Meow.')
    print(a, b, c)

if __name__ == '__main__': main()
