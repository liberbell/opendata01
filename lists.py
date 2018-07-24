#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    # i = game.index('Paper')
    # print(game[i])
    # game.insert(0,'Computer')
    # game.remove('Paper')
    # i = game.pop(3)
    # print(i)
    del game[1:3]
    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
