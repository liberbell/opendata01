#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import os
import random

def main():
    # v = sys.version_info
    # v = os.urandom(1).hex()
    x = random.randint(1, 100000)
    # print('Python version {}.{}.{}'.format(*v))
    print(x)

if __name__ == '__main__': main()
