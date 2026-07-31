#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' decorator_functiontiming.py

time relatively time consuming functions
with a decorator function
apply the decorator right above the function
you want to time, starting with a @
(use module timeit for faster functions)

more accurate (higher time resolution)...
time.perf_counter()  # needs python3.3 or higher

using the @wraps decorator on a decorator's inner function
is very helpful during debugging

tested using the SublimeText IDE on Linux  vegaseat  4jul2026
'''

import time
from functools import wraps

def print_timing(func):
    """set up a decorator function for timing"""
    @wraps(func)
    def wrapper(*arg):
        t1 = time.time()
        res = func(*arg)
        t2 = time.time()
        elapsed = (t2 - t1)*1e6
        fs = '{} took {:.3f} microseconds'
        print(fs.format(func.__name__, elapsed))       
        return res
    return wrapper

@print_timing
def get_primes(n):
    """
    standard optimized sieve algorithm to get a list
    of prime numbers from 2 to < n, prime numbers are
    only divisible by unity and themselves
    (1 is not considered a prime number)
    """
    if n < 2:  return []
    if n == 2: return [2]
    # do only odd numbers starting at 3
    s = list(range(3, n+1, 2))
    # n**0.5 simpler than math.sqr(n)
    mroot = n ** 0.5
    half = len(s)
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m*m-3)//2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i += 1
        m = 2*i+3
    # skip all zero items in list s
    return [2]+[x for x in s if x]


print( "prime numbers from 2 to <10,000,000 using a sieve algorithm")
prime_list = get_primes(10000000)

'''my result with Python32 -->
prime numbers from 2 to <10,000,000 using a sieve algorithm
get_primes took 2632.000 ms

just a note, result with Python27 -->
get_primes took 2394.000 ms

another note, result with Python364
get_primes took 1492.819 ms
'''


'''optional
print('-'*50)
print("test print just the first 15 primes:")
print(prime_list[:15])
print("... and the last 5 primes:")
print(prime_list[-5:])
'''
# higher time resolution ...

def print_timing_perf(func):
    '''
    create a timing decorator function
    use
    @print_timing_perf
    just above the function you want to time
    '''
    @wraps(func)
    def wrapper(*arg):
            # use high resolution perf_counter() 
            # needs python3.3 or higher
            start = time.perf_counter()  
            result = func(*arg)
            end = time.perf_counter()
            elapsed = (end - start) * 1e6
            fs = '{} took {:.3f} microseconds'
            print(fs.format(func.__name__, elapsed))
            return result
    return wrapper

@print_timing_perf
def get_primes2(n):
    """
    standard optimized sieve algorithm to get a list
    of prime numbers from 2 to < n, prime numbers are
    only divisible by unity and themselves
    (1 is not considered a prime number)
    """
    if n < 2:  return []
    if n == 2: return [2]
    # do only odd numbers starting at 3
    s = list(range(3, n+1, 2))
    # n**0.5 simpler than math.sqr(n)
    mroot = n ** 0.5
    half = len(s)
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m*m-3)//2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i += 1
        m = 2*i+3
    # skip all zero items in list s
    return [2]+[x for x in s if x]

print( "prime numbers from 2 to <10,000,000 using a sieve algorithm")
prime_list = get_primes2(10000000)

''' result ...
get_primes2 took 1478570.400 microseconds (us)
= 1478.570 milliseconds (ms)
'''
