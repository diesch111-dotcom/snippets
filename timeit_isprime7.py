#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' timeit_isprime7.py

Check the speed of seven isprime functions
updated

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

import sys
version_number = sys.version.split(' ')[0]
version_bits = '64bit' if sys.maxsize > 2**32 else '32bit'
print('Python version {} {}'.format(version_number, version_bits))

import timeit

def isprime1(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    return not any(n % x == 0 for x in range(3, int(n**0.5) + 1, 2))

def isprime2(n):
    '''
    check if integer n is a prime, return True or False
    '''
    # 2 is the only even prime
    if n == 2:
        return True
    # integers less than 2 and even numbers other than 2 are not prime
    elif n < 2 or not n & 1:
        return False
    #if n % 3 == 0: return False
    # loop looks at odd numbers 3, 5, 7, ... to sqrt(n)
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def isprime3(n):
    '''
    check if integer n is a prime, return True or False
    '''
    # 2 is the only even prime
    if n == 2:
        return True
    # integers less than 2 and even numbers other than 2 are not prime
    if n < 2:
        return False
    if not n & 1:  # even numbers
        return False
    # loop looks at odd numbers 3, 5, 7, ... to sqrt(n)
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def isprime4(n):
    '''
    check if integer n is a prime, return True or False
    uses a while loop, another way to write it, but is slower
    '''
    # 2 is the only even prime
    if n == 2:
        return True
    # integers less than 2 and even numbers other than 2 are not prime
    if n < 2:
        return False
    if n % 2 == 0:  # even numbers
        return False
    k = 3
    while k * k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

def isprime5(n):
    # deal with low primes and even numbers
    if n in (2,3,5,7,): return True
    if n < 2 or n%2 == 0: return False
    if n%3 == 0: return False
    # need divisors only up to sqrt(x) or n**0.5
    sqr = int(n**0.5)
    div = 5
    while div <= sqr:
        if n%div == 0: return False
        if n%(div+2) == 0: return False
        # loop every 6th integer
        div += 6
    return True

def isprime6(n):
    # no negative numbers
    n = abs(n)
    # deal with primes under 5
    if n in (2,3,):
        return True
    # the rest of the primes are multiples of 6 plus or minus 1
    # this eliminate 2/3 of the remaining candidates
    if (n < 5) or ((n % 6) not in (1, 5,)):
         return False
    # need divisors only up to math.sqrt(x)+2 (same as n**0.5+2)
    for div in range(6, int(n**0.5+2), 6):
        if (n % (div+1) == 0) or (n % (div-1) == 0):
            return False
    return True

import random

def isprime7(n, PROB=15):
    '''
    returns True if the number is prime.
    Failure rate: 1/4**PROB
    15 --> failure rate = 9.31e-10
    higher failure rate means higher speed
    '''
    if n==2: return True
    if n < 2 or n&1 == 0: return False
    s = 0
    d = n-1
    while 1&d == 0:
        s += 1
        d >>= 1
    for i in range(PROB):
        a = random.randint(2, n-1)
        composit = True
        if pow(a, d, n) == 1:
            composit = False
        if composit:
            for r in range(0, s):
                if pow(a, d*2**r, n) == n-1:
                    composit = False
                    break
        if composit: return False
    return True

def miller_rabin_isprime(n, ip=None, a=2):
    '''
    Miller-Rabin primality test
    very fast for large n
    returns a 1 if n is a prime
    does not test prime 2
    '''
    if ip == None:
        ip = n - 1  # standard
    if ip == 0:
        return 1
    x = miller_rabin_isprime(n, ip // 2)
    if x == 0:
        return 0
    y = (x * x) % n
    if ((y == 1) and (x != 1) and (x != (n - 1))):
        return 0
    if (ip % 2) != 0:
        y = (a * y) % n
    return y


# note 9999991 is a prime number, use it for testing
print("isprime1(9999991) = {}".format(isprime1(9999991)))
print("isprime2(9999991) = {}".format(isprime2(9999991)))
print("isprime3(9999991) = {}".format(isprime3(9999991)))
print("isprime4(9999991) = {}".format(isprime4(9999991)))
print("isprime5(9999991) = {}".format(isprime5(9999991)))
print("isprime6(9999991) = {}".format(isprime6(9999991)))
print("isprime7(9999991) = {}".format(isprime7(9999991)))

if miller_rabin_isprime(9999991) == 1:
    mr = True
else:
    mr = False
print("miller_rabin_isprime(9999991, 9999991-1) = {}".format(mr))

print("="*50)

passes = 1000

# warm up
stmt = 'isprime1(9999991)'
find_function = 'from __main__ import isprime1'
t = timeit.Timer(stmt, setup=find_function)
# gives the time in microseconds/pass
elapsed = (1_000_000 * t.timeit(number=passes)/passes)

stmt = 'isprime1(9999991)'
find_function = 'from __main__ import isprime1'
t = timeit.Timer(stmt, setup=find_function)
# gives the time in microseconds/pass
elapsed = (1_000_000 * t.timeit(number=passes)/passes)
print("%s takes %0.3f micro-seconds/pass" % (stmt, elapsed))

stmt = 'isprime2(9999991)'
find_function = 'from __main__ import isprime2'
t = timeit.Timer(stmt, setup=find_function)
# gives the time in microseconds/pass
elapsed = (1_000_000 * t.timeit(number=passes)/passes)
print("%s takes %0.3f micro-seconds/pass" % (stmt, elapsed))

stmt = 'isprime3(9999991)'
find_function = 'from __main__ import isprime3'
t = timeit.Timer(stmt, setup=find_function)
# gives the time in microseconds/pass
elapsed = (1_000_000 * t.timeit(number=passes)/passes)
print("%s takes %0.3f micro-seconds/pass" % (stmt, elapsed))

stmt = 'isprime4(9999991)'
find_function = 'from __main__ import isprime4'
t = timeit.Timer(stmt, setup=find_function)
# gives the time in microseconds/pass
elapsed = (1_000_000 * t.timeit(number=passes)/passes)
print("%s takes %0.3f micro-seconds/pass" % (stmt, elapsed))

stmt = 'isprime5(9999991)'
find_function = 'from __main__ import isprime5'
t = timeit.Timer(stmt, setup=find_function)
# gives the time in microseconds/pass
elapsed = (1_000_000 * t.timeit(number=passes)/passes)
print("%s takes %0.3f micro-seconds/pass" % (stmt, elapsed))

stmt = 'isprime6(9999991)'
find_function = 'from __main__ import isprime6'
t = timeit.Timer(stmt, setup=find_function)
# gives the time in microseconds/pass
elapsed = (1_000_000 * t.timeit(number=passes)/passes)
print("%s takes %0.3f micro-seconds/pass" % (stmt, elapsed))

stmt = 'isprime7(9999991)'
find_function = 'from __main__ import isprime7'
t = timeit.Timer(stmt, setup=find_function)
# gives the time in microseconds/pass
elapsed = (1_000_000 * t.timeit(number=passes)/passes)
print("%s takes %0.3f micro-seconds/pass" % (stmt, elapsed))

stmt = 'miller_rabin_isprime(9999991, 9999991-1)'
find_function = 'from __main__ import miller_rabin_isprime'
t = timeit.Timer(stmt, setup=find_function)
# gives the time in microseconds/pass
elapsed = (1_000_000 * t.timeit(number=passes)/passes)
print("%s takes %0.3f micro-seconds/pass" % (stmt, elapsed))


Python version 3.12.3 64bit
isprime1(9999991) = True
isprime2(9999991) = True
isprime3(9999991) = True
isprime4(9999991) = True
isprime5(9999991) = True
isprime6(9999991) = True
isprime7(9999991) = True
miller_rabin_isprime(9999991, 9999991-1) = True
==================================================
isprime1(9999991) takes 77.601 micro-seconds/pass
isprime2(9999991) takes 60.504 micro-seconds/pass
isprime3(9999991) takes 58.337 micro-seconds/pass
isprime4(9999991) takes 99.101 micro-seconds/pass
isprime5(9999991) takes 44.820 micro-seconds/pass
isprime6(9999991) takes 46.304 micro-seconds/pass
isprime7(9999991) takes 31.067 micro-seconds/pass
miller_rabin_isprime(9999991, 9999991-1) takes 4.255 micro-seconds/pass''' 
...

'''
