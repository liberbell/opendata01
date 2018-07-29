#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    try:
        x = 5/0
    except ValueError:
        print('I caught a ValueError')
    except ZeroDivisionError:
        print('Don\'t divide by zero')
    # print('Hello, World.')

if __name__ == '__main__': main()
