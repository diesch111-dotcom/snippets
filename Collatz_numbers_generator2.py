#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Collatz_numbers_generator2.py

Collatz numbers (the famous 3n+1 problem, by  L. Collatz 1937)

Take any number, if even divide it by 2,
if odd multiply it by 3 and add one,
should converge to 2

vegaseat 15oct2026
"""

def gen_Collatz(n):
    '''
    a Collatz numbers generator
    take any number n, if even divide it by 2,
    if odd multiply it by 3 and add one,
    should converge to 2
    '''
    while n > 1:
        yield n
        # check if n is even
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1


# start with n
n = 7
for x in gen_Collatz(n):
    print(x, end=" ")

print('')

''' result...
7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2
'''