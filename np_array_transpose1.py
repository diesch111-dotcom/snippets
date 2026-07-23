#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' np_array_transpose1.py

Transpose a 2D_array (list of lists) from 4x6 to 6x4 with transpose()

doc
https://scipy.github.io/old-wiki/pages/Numpy_Example_List_With_Doc.html

in the LinuxMint terminal use ...
sudo apt-get install python3-numpy
if needed

tested ++ using the Spyder IDE on Linux  dns aka vegaseat  4jul2026
'''

import numpy as np

arr_4x6 = [
[0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 0],
[0, 0, 0, 1, 1, 0],
[0, 1, 0, 1, 1, 0],
]

print('original 4 row by 6 column numpy array:')
a_4x6 = np.array(arr_4x6)
print(a_4x6)

print('-'*20)

print('applying transpose() switches rows to columns:')
a_6x4 = a_4x6.transpose()
print(a_6x4)

print('-'*20)

print('convert back to a Python list with tolist():')
arr_6x4 = a_6x4.tolist()

for row in arr_6x4:
    print(row)

"""
original 4 row by 6 column numpy array:
[[0 0 0 0 0 0]
 [0 1 1 1 1 0]
 [0 0 0 1 1 0]
 [0 1 0 1 1 0]]
--------------------
applying transpose() switches rows to columns:
[[0 0 0 0]
 [0 1 0 1]
 [0 1 0 0]
 [0 1 1 1]
 [0 1 1 1]
 [0 0 0 0]]
--------------------
convert back to a Python list with tolist():
[0, 0, 0, 0]
[0, 1, 0, 1]
[0, 1, 0, 0]
[0, 1, 1, 1]
[0, 1, 1, 1]
[0, 0, 0, 0]
"""