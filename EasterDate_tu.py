#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' EasterDate_tu.py

A program to calculate date of Easter for a given year 1982-2048

SublimeText IDE has problems with Python input(), so use module turtle
turtle.numinput(title, prompt, default=None, minval=None, maxval=None)

tested with SublimeText IDE on LinuxMint  vegaseat 15jun2026
'''

# SublimeText IDE has problems with Python input()
# so use module turtle
import turtle as tu
tu.Screen().setup(15, 15)
title = "Year"
prompt = "Enter a year 1982-2048"
year = int(tu.numinput(title, prompt, minval=1982, maxval=2048))

def calc_easter(year):
    if year in range(1982, 2049):
        a = year % 19
        b = year % 4
        c = year % 7
        d = ((19*a) + 24)%30
        e = ((2*b) + (4*c) + (6*d) + 5)%7
        f = 22 + d + e
        if f <= 31:
            print("Easter {} is on March {}".format(year, f))
        else:
            print("Easter {} is on April {}".format(year,f - 31))
    else:
        print("Year is not within range")


#year = int(input('Enter a year between 1982-2048 '))
calc_easter(year)

''' possible result...
Easter 2026 is on April 5
'''
