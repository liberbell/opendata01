#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempts = 3

while pw != secret:
    count +=1
    if count > max_attempts: break
    pw = input(f"{count}: What's the secret word? ")
