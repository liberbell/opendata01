#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = dict(kitten = 'meow',puppy = 'ruff!', lion= 'grrr',
        giraffe = 'I am a giraffe!', dragon = 'rawr')
    # animals['lion'] = 'I am a lion'
    # animals['monkey'] = 'hah'
    print('found!' if 'lion' in animals else 'nope')
    print('found!' if 'gozilla' in animals else 'nope')
    print(animals.get('gadzilla'))
    # print(animals['lion'])
    # for v in animals.values(): print(v)
    # for k in animals.keys(): print(k)
    # for k, v in animals.items():
    #     print(f'{k}: {v}')
    # animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
    #     'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    print_dict(animals)

def print_dict(o):
    for k, v in o.items(): print(f'{k}: {v}')

if __name__ == '__main__': main()
