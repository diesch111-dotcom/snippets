#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" concurrent_futures2.py

check larger possible primes concurrently,
speed is almost instant!

vegaseat  16oct2026
"""

import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    ''' check if n is a prime number'''
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    # uses the multiprocessing module which side-steps the
    # Global Interpreter Lock (GIL) this means only
    # picklable objects can be executed and returned
    # defaults to the number of processors on the machine
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f'{number} is prime: {prime}')

if __name__ == '__main__':
    main()

''' result...
112272535095293 is prime: True
112582705942171 is prime: True
112272535095293 is prime: True
115280095190773 is prime: True
115797848077099 is prime: True
1099726899285419 is prime: False
'''
