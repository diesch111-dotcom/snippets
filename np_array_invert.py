#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' np_array_invert.py

Invert a numpy array

doc
https://scipy.github.io/old-wiki/pages/Numpy_Example_List_With_Doc.html

in the LinuxMint terminal use ...
sudo apt-get install python3-numpy
python3-numpy is already the newest version (1:1.26.4+ds-6ubuntu1).

tested ++ using the Spyder IDE on Linux  dns aka vegaseat  4jul2026
'''

import numpy as np

a = np.matrix([[1, 2, 3],
[2, 3, 4],
[3, 4, 5]], dtype=float)

print(a)

'''
[[1. 2. 3.]
 [2. 3. 4.]
 [3. 4. 5.]]
'''

print('='*50)

# inverted matrix (a has to be square)
print(np.linalg.inv(a))
#print('='*50)
# or
#print(a ** (-1))

'''
[[-4.50359963e+15  9.00719925e+15 -4.50359963e+15]
 [ 9.00719925e+15 -1.80143985e+16  9.00719925e+15]
 [-4.50359963e+15  9.00719925e+15 -4.50359963e+15]]
'''

print('='*50)

print(a * np.linalg.inv(a))

print('-'*20)
# or
print(np.dot(a, a ** (-1)))

'''
[[ 0.  0.  0.]
 [ 4.  0. -2.]
 [ 0.  0.  0.]]
--------------------
[[ 0.  0.  0.]
 [ 4.  0. -2.]
 [ 0.  0.  0.]]
'''

print('-'*50)

print(np.linalg.pinv(a))

'''
[[-1.08333333e+00 -1.66666667e-01  7.50000000e-01]
 [-1.66666667e-01  3.67761377e-16  1.66666667e-01]
 [ 7.50000000e-01  1.66666667e-01 -4.16666667e-01]]
'''