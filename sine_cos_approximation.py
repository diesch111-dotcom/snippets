#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' sine_cos_approximation.py

approximation of sine using a series expansion
Taylor (Maclaurin) series:
sin(x) = x - x**3/3! + x**5/5! - x**7/7! + ...

cos(x) = 1 - x**2/2! + x**4/4! - x**6/6! - ...

tan(x) = sin(x)/cos(x)

sin(0) = 0
cos(0) = 1
sin(x)**2 + cos(x)**2 = 1

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

import math  # for comparison

def sine(x):
    term = float(x)
    result = term
    u = - term * term
    n = 0
    # loop until term gets to be very small
    while abs(term) > 1.0e-10:
        n += 1
        # keep the denominator factorial as integer
        term *= u / ((2*n) * (2*n+1))
        result += term
    return result

# x is the angle in radians
x = 0.5

print(sine(x))      # 0.4794255386041834
print(math.sin(x))  # 0.479425538604203

# cosine ..

theta = 45
x = math.radians(theta)
cosx = 1
alt = 1
for n in range(2, 15, 2):
    # alternate between 1 and -1
    alt *= -1
    cosx += alt*math.pow(x, n)/math.factorial(n)
    #print(cosx)  # test

print("Approximate cos({}) = {}".format(theta, cosx))
print("Module math cos({}) = {}".format(theta, math.cos(x)))

''' result ...
Approximate cos(45) = 0.707106781187
Module math cos(45) = 0.707106781187
'''