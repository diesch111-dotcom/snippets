#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" power_series_Euler2.py

Power series for Euler's number (base of natural logs)
e = 1 + x * x*2.0/2 + x*3.0/(2*3) + x*4.0/(2*3*4) ...

vegaseat  16oct2026
"""

x = 1.0
f = 1
qe = 0.0
for n in range(1, 32):
    f *= n
    qe += x*n/f


print("power series e = %0.30f" % qe)
# compare ...
import math
# only goes to 12 decimals
print("Python  math.e = %0.12f" % math.e)

''' result...
power series e = 2.718281828459045534884808148490
Python  math.e = 2.718281828459
'''
