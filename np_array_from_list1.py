#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' np_array_from_list1.py

Convert a Python list to a numpy array and then a text string

in the LinuxMint terminal use ...
sudo apt-get install python3-numpy
if need be

tested ++ using the Spyder IDE on Linux  dns aka vegaseat  4jul2026
'''

import numpy as np

mylist = [
[1000, 2, 3],
[4, 5000, 6],
[7, 8, 9000]
]

# create a numpy array from a corresponding Python list object
np_arr = np.array(mylist)

print(np_arr)

'''
[[1000    2    3]
 [   4 5000    6]
 [   7    8 9000]]
'''

# np.array_str(a, max_line_width=None, precision=None, suppress_small=None) 
# convert to a text string
arr_str = np.array_str(np_arr)

sf = """
change the numpy array into a string
%s
"""
print(sf % arr_str)

'''
change the numpy array into a string
[[1000    2    3]
 [   4 5000    6]
 [   7    8 9000]]
'''