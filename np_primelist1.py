#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' np_primelist1.py
create a numpy array of prime numbers < limit
very fast algorithm

doc
https://scipy.github.io/old-wiki/pages/Numpy_Example_List_With_Doc.html

in the LinuxMint terminal use ...
sudo apt-get install python3-numpy
if need be

tested ++ using the Spyder IDE on Linux  dns aka vegaseat  4jul2026
'''

import numpy as np

def np_primes1(limit):
    """returns a numpy array of primes, 2 <= p < limit"""
    # create a sieve of ones
    is_prime = np.ones(limit + 1, dtype=bool)
    for n in range(2, int(limit**0.5 + 1.5)):
        if is_prime[n]:
            is_prime[n*n::n] = 0
    return np.nonzero(is_prime)[0][2:]

print("first 10 primes:")
print(np_primes1(1000000)[:10])
print("last 5 primes (less than 1000000):")
print(np_primes1(1000000)[-5:])
print("convert first 10 primes to a list:")
print(list(np_primes1(1000000)[:10]))

''' result...
first 10 primes:
[ 2  3  5  7 11 13 17 19 23 29]
last 5 primes (less than 1000000):
[999953 999959 999961 999979 999983]
convert first 10 primes to a list:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
'''