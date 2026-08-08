#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Newton_method.py

find value for x in f(x) = 0 using Newton's method

tested with Spyder IDE on LinuxMint  vegaseat 15jun2026
'''

def derivative(f):
    def compute(x, dx):
        return (f(x+dx) - f(x))/dx
    return compute

def newtons_method(f, x, dx=0.000001, tolerance=0.000001):
    '''f is the function f(x)'''
    df = derivative(f)
    while True:
        x1 = x - f(x)/df(x, dx)
        t = abs(x1 - x)
        if t < tolerance:
            break
        x = x1
    return x

def f(x):
    '''
    here solve x for ...
    x*x - 7 = 0
    same as x = 7**0.5 = sqrt(7)
    '''
    return x*x - 7

x_approx = 1  # rough guess
# f refers to the function f(x)
x = newtons_method(f, x_approx)

print("Solve for x in x*x - 7 = 0  or  x = sqrt(7)")
print("%0.12f (x via Newton)" % x)
# compare with math.sqrt(7)
import math
print("%0.12f (x via sqrt(7))" % math.sqrt(7))

''' result...
Solve for x in x*x - 7 = 0  or  x = sqrt(7)
2.645751311114 (x via Newton)
2.645751311065 (x via sqrt(7))
'''
