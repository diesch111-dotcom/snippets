#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" frange2.py

A range() generator that handles floating point numbers
Uses delta fuzzy logic to avoid floating point rep. errors

vegaseat  26oct2026
"""

def frange(start, stop=None, step=1.0, delta=0.0000001):
    """
    frange( [start,] stop[, step] )
    a range generator that handles floating point numbers
    uses delta fuzzy logic to avoid float rep errors
    eg. stop=6.4 --> 6.3999999999999986 would otherwise slip through
    """
    # if start is missing it defaults to zero
    if stop == None:
        stop = start
        start = 0.0
    # allow for decrement
    if step <= 0:
        while start > (stop + delta):
            yield start
            start += step
    else:
        while start < (stop - delta):
            yield start
            start += step


# testing...
for x in frange(17, 4, -2.9):
    print(x)

'''
17
14.1
11.2
8.299999999999999
5.399999999999999
'''

print('='*20)

for x in frange(6.0, 6.4, 0.1):
    print(x)

'''
6.0
6.1
6.199999999999999
6.299999999999999
'''

