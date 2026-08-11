#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' difflib_str_match_percent.py

Evaluate two text strings and get a percent of match,
using Python module difflib

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

import difflib

def percent_match(text1, text2):
    '''
    evaluate two text strings and return a percent of match
    '''
    sqm = difflib.SequenceMatcher(None, text1, text2)
    matchratio = sqm.ratio()
    matchpercent = matchratio * 100
    return matchpercent


text1 = """\
Mary had a little lamb
its fleece was white as snow
and everywhere that Mary went
the lamb was sure to go"""

text2 = """\
Mary has a little lamp
his fleece as white as snow
and where ever that Mary went
the lamp is sure to go"""

matchpercent = percent_match(text1, text2)

print(text1)
print('-'*30)
print(text2)
print('-'*30)
print("The two texts match %0.2f percent" % matchpercent)
'''
Mary had a little lamb
its fleece was white as snow
and everywhere that Mary went
the lamb was sure to go
------------------------------
Mary has a little lamp
his fleece as white as snow
and where ever that Mary went
the lamp is sure to go
------------------------------
The two texts match 89.42 percent
'''
