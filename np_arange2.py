#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' np_arange2.py

using module numpy arange() function for a floating point array
numpy arange(start, end, step)
module numpy (numeric python extensions, high speed)

doc
https://scipy.github.io/old-wiki/pages/Numpy_Example_List_With_Doc.html

in the LinuxMint terminal use ...
sudo apt-get install python3-numpy
if needed

tested ++ using the Spyder IDE on Linux  dns aka vegaseat  4jul2026
'''

import numpy as np
import math

# numpy arange(start, end, step)
myarray = np.arange(0.5, math.sqrt(2), 0.1)

print(myarray)

# {:f} avoids some of the rundoff problems with floats
for item in myarray: 
    print('{:f}'.format(item))

''' result...
[0.5 0.6 0.7 0.8 0.9 1.  1.1 1.2 1.3 1.4]
0.500000
0.600000
0.700000
0.800000
0.900000
1.000000
1.100000
1.200000
1.300000
1.400000
'''
