#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempts = 5

while pw != secret:
    count +=1
    if count > max_attempts: break
    if count == 3:continue
    pw = input(f"{count}: What's the secret word? ")
else:
    auth = True

print("Authorised" if auth else "calling the FBI")
