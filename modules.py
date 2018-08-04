#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import os

def main():
    # v = sys.version_info
    v = os.urandom(25)
    # print('Python version {}.{}.{}'.format(*v))
    print(v)

if __name__ == '__main__': main()
