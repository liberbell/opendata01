#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# def main():
#     print('Hello,World. {}' .format(42 * 7))
#
# if __name__ == '__main__': main()
class Mystring(str):
    def __str__(self):
        return self[::-1]

s = Mystring('Hello World.')
print(s)
