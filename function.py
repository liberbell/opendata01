#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = kitten()
    print(type(x), x)

def kitten():
    print('Meow.')
    return (42, 43 ,44)

if __name__ == '__main__': main()
