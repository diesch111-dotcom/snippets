#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' dict_3darray_keys.py

create a 3x4x2 3D-array using a dictionary with (x,y,z):value pairs_keys
tested with SublimeText IDE on LinuxMint  vegaseat 15jun2026
'''

import pprint

# initializes values to zero
arr3d = dict(((x,y,z), 0) for x in range(3) for y in range(4)
    for z in range(2)) 
# Python3 has dictionary comprehension...
#arr3d = {(x,y,z):0 for x in range(3) for y in range(4) 
#    for z in range(2)}

pprint.pprint(arr3d)

"""
{(0, 0, 0): 0,
 (0, 0, 1): 0,
 (0, 1, 0): 0,
 (0, 1, 1): 0,
 (0, 2, 0): 0,
 (0, 2, 1): 0,
 (0, 3, 0): 0,
 (0, 3, 1): 0,
 (1, 0, 0): 0,
 (1, 0, 1): 0,
 (1, 1, 0): 0,
 (1, 1, 1): 0,
 (1, 2, 0): 0,
 (1, 2, 1): 0,
 (1, 3, 0): 0,
 (1, 3, 1): 0,
 (2, 0, 0): 0,
 (2, 0, 1): 0,
 (2, 1, 0): 0,
 (2, 1, 1): 0,
 (2, 2, 0): 0,
 (2, 2, 1): 0,
 (2, 3, 0): 0,
 (2, 3, 1): 0}
"""

print('-'*20)

# change some values, basically assign to index
arr3d[2, 1, 0] = 550
arr3d[1, 0, 1] = 1700
# or ...
ix = (0, 0, 0)
arr3d[ix] = 99
# or just ...
ix = 1, 1, 1
arr3d[ix] = 303

pprint.pprint(arr3d)

"""my output -->
{(0, 0, 0): 99,
 (0, 0, 1): 0,
 (0, 1, 0): 0,
 (0, 1, 1): 0,
 (0, 2, 0): 0,
 (0, 2, 1): 0,
 (0, 3, 0): 0,
 (0, 3, 1): 0,
 (1, 0, 0): 0,
 (1, 0, 1): 1700,
 (1, 1, 0): 0,
 (1, 1, 1): 303,
 (1, 2, 0): 0,
 (1, 2, 1): 0,
 (1, 3, 0): 0,
 (1, 3, 1): 0,
 (2, 0, 0): 0,
 (2, 0, 1): 0,
 (2, 1, 0): 550,
 (2, 1, 1): 0,
 (2, 2, 0): 0,
 (2, 2, 1): 0,
 (2, 3, 0): 0,
 (2, 3, 1): 0}
"""

print('-'*20)

# get a specific value from a given index
print(arr3d[1, 1, 1])  # 303
# or ...
ix = 0, 0, 0
print(arr3d[ix])  # 99

print('-'*20)

# get the lowest and highest key
low = min(arr3d.keys())    # --> (0, 0, 0)
heigh = max(arr3d.keys())  # --> (2, 3, 1)
# show values
print( "ix=%s val=%s" % (low, arr3d[low]) )
print( "ix=%s val=%s" % (heigh, arr3d[heigh]) )

print('get the heighest value in the array:')
print(max(arr3d.values()))  # 1700
