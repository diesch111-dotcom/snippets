#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' gmpy2_factorial.py

gmpy2.fac(n) returns the exact factorial of n

gmpy is a C-coded Python extension module that supports fast
multiple-precision arithmetic, 

Advanced Number Theory: It comes out of the box with highly optimized
functions for primality testing (is_prime), greatest common divisors (gcd), 
modular inverse, and factorials.  

use Linux Software Manager to install  Python3-gmpy2
 
tested ++ using the Spyder IDE on Linux OS  dns aka vegaseat  13jul2026
'''

import gmpy2
from gmpy2 import mpz
import math

n = 50
print("gmpy2.fac({}) = \n{}".format(n, gmpy2.fac(n)))

# compare to math.factorial
print(math.factorial(n))

''' result (compared to math.factorial())...
gmpy2.fac(50) =
30414093201713378043612608166064768844377641568960512000000000000
30414093201713378043612608166064768844377641568960512000000000000
'''

# 1. High-speed, large integer math
# Calculates 2 to the millionth power incredibly fast
large_num = mpz(2) ** 1000000  

# 2. Fast primality checking (uses probabilistic tests)
print(gmpy2.is_prime(997))  # Returns: True

# 3. Arbitrary-precision floating point
# Set precision to 100 bits
gmpy2.get_context().precision = 100  
# Prints Pi out to your exact specified precision
print(gmpy2.const_pi())  

'''
3.1415926535897932384626433832793
'''
