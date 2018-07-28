#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    seq = range(11)
    from math import pi
    # seq2 = [round(pi,i) for i in seq]
    seq2 = {x: x**2 for x in seq}
    print_list(seq)
    print(seq2)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()
