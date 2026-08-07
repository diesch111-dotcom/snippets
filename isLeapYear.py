#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' isLeapYear.py

Rule...
all years divisible by 400 are leap years	
all remaining years divisible by 100 are not leap years
all remaining years divisible by 4 are leap years

tested with Spyder IDE on LinuxMint  vegaseat 15jun2026
'''

def isLeapYear1(year):
    """
    return True if year is a leap year
    this syntax needs Python25 or higher
    """
    return False if year%4 else True if year%100 else not year%400

def isLeapYear2(year):
    """
    return True if year is a leap year
    """
    return (not year%4 and year%100 or not year%400) and True

def isLeapYear3(year):
    """
    return True if year is a leap year (shows details)
    """
    # only years divisible by 4 are potential leap years
    # if it has a remainder return False
    if (year % 4): return False
    # all years divisible by 400 are leap years	
    if (not year % 400): return True
    # all other years divisible by 100 are not leap years
    if (not year % 100): return False
    # remaining years divisible by 4 are leap years
    return True

def isLeapYear4(year):
    """
    follows the rule ...
    all years divisible by 400 are leap years	
    all remaining years divisible by 100 are not leap years
    all remaining years divisible by 4 are leap years
    all remaining years are not leap years    
    """
    if year % 400 == 0: return True
    elif year % 100 == 0: return False
    elif year % 4 == 0: return True
    else: return False

# clever ...
import datetime as dt
def isLeapYear5(year):
    """
    return True if year is a leap year
    """
    try: 
        # if Feb29 exists for that year it is a leapyear
        dt.date(year, 2, 29)
        return True
    except: 
        return False


# testing ...
year = 2000
print("year = %d" % year)
print(isLeapYear1(year))
print(isLeapYear2(year))
print(isLeapYear3(year))
print(isLeapYear4(year))
print(isLeapYear5(year))

year = 1900
print("year = %d" % year)
print(isLeapYear1(year))
print(isLeapYear2(year))
print(isLeapYear3(year))
print(isLeapYear4(year))
print(isLeapYear5(year))

year = 1912
print("year = %d" % year)
print(isLeapYear1(year))
print(isLeapYear2(year))
print(isLeapYear3(year))
print(isLeapYear4(year))
print(isLeapYear5(year))

""" result...
year = 2000
True
True
True
True
True
year = 1900
False
False
False
False
False
year = 1912
True
True
True
True
True
"""
