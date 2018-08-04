#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import os
import random
import datetime

def main():
    # v = sys.version_info
    # v = os.urandom(1).hex()
    # x = random.randint(1, 100000)
    x = list(range(25))
    # print('Python version {}.{}.{}'.format(*v))
    print(x)
    random.shuffle(x)
    print(x)

    now = datetime.datetime.now()
    print(now.year, now.month, now.day, now.hour, now.minute)

if __name__ == '__main__': main()
