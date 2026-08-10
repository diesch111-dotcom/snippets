#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pi_approximate_decimal.py

This is from the Python manual documentation of the decimal module

see also:
https://mpmath.org/doc/0.19/functions/constants.html

pi is circumference of a circle with diameter = 1 (unitcircle)
pi is the area of a circle that fits inside a 3-4-5 triangle

works with LinuxMint and Spyder IDE  dns(vegaseat)  15jun2026

'''

import decimal

def pi_decimal(prec):
    """
    from the decimal.py documentation
    """
    decimal.getcontext().prec = prec + 2
    D = decimal.Decimal
    # tuple swap
    lasts, t, s, n, na, d, da = D(0), D(3), D(3), D(1), D(0), D(0), D(24)
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    decimal.getcontext().prec -= 2
    # unary plus applies the new precision
    return +s


precision = 60
print("pi calculated to a precision of {}".format(precision))
print(pi_decimal(precision))
print("compare with published pi")
print("3.14159265358979323846264338327950288419716939937510582097494")

'''
pi calculated to a precision of 60
3.14159265358979323846264338327950288419716939937510582097494
compare with published pi
3.14159265358979323846264338327950288419716939937510582097494
'''

# for comparison ...
import mpmath as mpm

print("mpmath pi to 60 decimals:")
# set precision in decimal points
mpm.mp.dps = 60
print(mpm.pi())
'''
mpmath pi to 60 decimals:
3.14159265358979323846264338327950288419716939937510582097494
'''
