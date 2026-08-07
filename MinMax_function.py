#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' MinMax_function.py

Find the min and max values of
f(x) = (2*x*x*x) - (8*x*x) + x + 16
over a x range of -1 to 3

tested with Spyder IDE on LinuxMint  vegaseat 15jun2026
'''

def frange(start, stop=None, step=1.0, delta=0.0000001):
    """
    a range generator that handles floating point numbers
    uses delta fuzzy logic to avoid float rep errors
    eg. stop=6.4 --> 6.3999999999999986 would slip through
    """
    # if start is missing it defaults to zero
    if stop == None:
        stop = start
        start = 0
    # allow for decrement
    if step <= 0:
        while start > (stop + delta):
            yield start
            start += step
    else:
        while start < (stop - delta):
            yield start
            start += step

def func(x):
    y = (2*x*x*x) - (8*x*x) + x + 16
    return y

# create a list of (y, x) tuples
# over a range of floating point numbers
start = -1
step = 0.0001
# stop at 3 inclusive (add a delta value)
stop = 3 + 0.0000001
q = []
for x in frange(start, stop, step):
    y = func(x)
    q.append((y, x))

y_min = min(q)
y_max = max(q)

print("y = f(x) = (2*x*x*x) - (8*x*x) + x + 16")
print( "Minimum y = %0.6f at x = %0.6f" % y_min )
print( "Maximum y = %0.6f at x = %0.6f" % y_max )

""" result...
y = f(x) = (2*x*x*x) - (8*x*x) + x + 16
Minimum y = -0.328053 at x = 2.602600
Maximum y = 16.031756 at x = 0.064000
"""