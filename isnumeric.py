#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' isnumeric.py

Test a numeric string str if it's usable for int(str) or float(str)
An attempt to make this fool proved!

In Europe they use ',' instead of '.'

tested with Spyder IDE on LinuxMint  vegaseat 15jun2026
'''

def isnumeric(str):
    '''returns True if string s is numeric'''
    if str.count('.') > 1: return False
    if str.count('-') > 1: return False
    if str.count('+') > 1: return False
    return all(c in "0123456789.+-" for c in str) and \
        any(c in "0123456789" for c in str)

# testing...
if __name__ == '__main__':
    print(isnumeric('123'))      # True
    print(isnumeric('-123.45'))  # True
    print(isnumeric('+3.14'))    # True
    print(isnumeric('$99.95'))   # False
    print(isnumeric('.'))        # False
    print(isnumeric('1.2.3'))    # False
