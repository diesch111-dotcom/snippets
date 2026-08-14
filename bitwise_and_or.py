#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' bitwise_and_or.py

some interesting applications of bitwise and (&), or (|), exclusive or (^)

tested with VSCodium IDE on LinuxMint  VegasEat 19jul2026
'''

def is_odd(n):
    '''
    symbol & is the bitwise 'and' operator
    use n & 1 to check if n is odd or even
    return True if n is an odd integer, else False
    '''
    if n & 1:
        return True
    else:
        return False

def next_odd(n):
    '''
    symbol | is the bitwise 'or' operator
    use n | 1 to turn an even integer into its next odd integer
    does not change odd integers
    '''
    return n|1

def next_odd_even(n):
    '''
    symbol ^ is the bitwise 'exlusive or' operator
    use n ^ 1 to turn an even n into the next odd integer
    and an odd n into the previous even integer
    '''
    return n^1


# testing ...
print(f"{is_odd(21) = }")  # is_odd(21) = True
print(f"{is_odd(22) = }")  # is_odd(22) = False

print(f"next_odd(8) = {next_odd(8) = }")  # next_odd(8) = 9
print(f"next_odd(7) = {next_odd(7) = }")  # next_odd(7) = 7

print(f"{next_odd_even(8) = }")  # next_odd_even(7) = 9
print(f"{next_odd_even(7) = }")  # next_odd_even(7) = 6

