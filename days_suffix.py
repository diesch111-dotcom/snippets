#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' days_suffix.py

Add the proper suffix to days of a month
the suffix list index coincides with the day number

tested with SublimeText IDE on LinuxMint  vegaseat 15jun2026
'''

# list_1to10 also holds true for list_21to30
list_1to10 = ['st', 'nd', 'rd'] + ['th']*7
# 11th to 13th are exceptions
list_11to20 = ['th']*10

# suffix list for numbers 0 to 31
sx_list = ['th'] + list_1to10 + list_11to20 + (list_1to10) + ['st']

#print(sx_list)

# test it
for x in range(1, 32):
    print( "%d%s" % (x, sx_list[x]) )

'''
1st
2nd
3rd
4th
5th
6th
7th
8th
9th
10th
11th
12th
13th
14th
15th
16th
17th
18th
19th
20th
21st
22nd
23rd
24th
25th
26th
27th
28th
29th
30th
31st
'''