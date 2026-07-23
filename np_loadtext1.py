#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' np_loadtext1.py

load a csv (comma separated value) file into an array
via loadtxt()

doc
https://scipy.github.io/old-wiki/pages/Numpy_Example_List_With_Doc.html

in the LinuxMint terminal use ...
sudo apt-get install python3-numpy
if need be

tested ++ using the Spyder IDE on Linux  dns aka vegaseat  4jul2026
'''

import numpy as np

'''
make sure myfile.csv is in the working directory
myfile.csv looks like this ...
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
21,22,23,24,25,26,27,28,29,210,211,212,213,214,215,216,217,218,219
31,32,33,34,35,36,37,38,39,310,311,312,313,314,315,316,317,318,319
41,42,43,44,45,46,47,48,49,410,411,412,413,414,415,416,417,418,419
51,52,53,54,55,56,57,58,59,510,511,512,513,514,515,517,516,518,519
'''

# 32 bit signed integer
x = np.dtype('i4')
print(x.base)
# same as 'f8' a 64 bit floating point number
f = np.dtype(float)
print(f.base)
# string (byte string in Python3) of length 5
s = np.dtype('S5')
print(s)

'''
int32
float64
|S5
'''

# loads file myfile.csv dierctly from the working directory
# default dtype is float
a,b,c = np.loadtxt('myfile.csv', delimiter=',', usecols=(0,12,18),
                   skiprows=1, unpack=True)
print(a, b, c)

'''
[21. 31. 41. 51.] [213. 313. 413. 513.] [219. 319. 419. 519.]
'''

print('-'*60)

# default dtype is float
arr = np.loadtxt('myfile.csv', delimiter=',', usecols=(0,12,18),
                 skiprows=0, unpack=False)
print(arr)

'''
[[  1.  13.  19.]
 [ 21. 213. 219.]
 [ 31. 313. 319.]
 [ 41. 413. 419.]
 [ 51. 513. 519.]]
'''

print('-'*60)

# set dtype to integer 'i4'
arr_int = np.loadtxt('myfile.csv', delimiter=',', usecols=(0,12,18),
                 skiprows=0, dtype=('i4') , unpack=False)
print(arr_int)

'''
[[  1  13  19]
 [ 21 213 219]
 [ 31 313 319]
 [ 41 413 419]
 [ 51 513 519]]
'''

print('-'*60)

# use mixed dtypes 'S5, i4, S8'
arr_mix = np.loadtxt('myfile.csv', delimiter=',', usecols=(0,12,18),
                 skiprows=1, dtype=('S5, i4, S8'), unpack=False)
print(arr_mix)
'''
[(b'21', 213, b'219') (b'31', 313, b'319') (b'41', 413, b'419')
 (b'51', 513, b'519')]
'''

#help(np.dtype)