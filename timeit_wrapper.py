#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' timeit_wrapper.py

Timing functions with a timeit wrapper

Changed in version 3.3: 
time.perf_counter() is now the default timer

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

import sys
version_number = sys.version.split(' ')[0]
version_bits = '64bit' if sys.maxsize > 2**32 else '32bit'
print('Python version {} {}'.format(version_number, version_bits))


def get_time(fs, number=10000, module="__main__"):
    """
    this wrapper can be used to time any function
    pass full function call in as a string eg. 'func(arg1, arg2)'
    number = number of timeit loops
    module namespace is autodetected
    works with Python2 and Python3
    """
    import timeit
    import inspect
    # extract function name
    q1 = fs.split('(')
    f = eval(q1[0])
    # extract arguments
    q2 = q1[1].strip(')')
    if q2:
        args = eval(q2)
    else:
        args = None
    name = f.__name__
    # get module namespace
    module = inspect.getmodule(f).__name__
    if args == None:
        st1 = "%s()" % (name)
    elif type(args) == tuple:
        st1 = "%s%s" % (name, args)
    elif type(args) == str:
        st1 = "%s('%s')" % (name, args)
    else:
        st1 = "%s(%s)" % (name, args)
    st2 = "from %s import %s" % (module, name)
    t = timeit.Timer(st1, st2)
    # elapsed time is in microseconds
    print( "Function %s took %.2f microseconds/pass" % \
        (st1, 1_000_000*t.timeit(number=number)/number) )
    # optional ...
    return eval(fs)

def permutate3(mystr):
    """
    accepts a string as input and
    returns a list of permutated strings
    """
    if len(mystr) <= 1:
        return [mystr]
    # also recursive
    return [x[:p] + mystr[0] + x[p:] for x in permutate3(mystr[1:])\
        for p in range(len(x) + 1)]


my_str = "bush"

print(get_time("permutate3(my_str)"))

""" result...
Python version 3.12.3 64bit
Function permutate3('bush') took 6.96 microseconds/pass
['bush', 'ubsh', 'usbh', 'ushb', 'bsuh', 'sbuh', 'subh', 'suhb', 'bshu', 'sbhu', 'shbu', 'shub', 'buhs', 'ubhs', 'uhbs', 'uhsb', 'bhus', 'hbus', 'hubs', 'husb', 'bhsu', 'hbsu', 'hsbu', 'hsub']
"""

def use_timeit(stmt, setup, passes=1000):
    """
    use module timeit to time a statement stmt
    setup gives information where too find variables/functions
    for time consuming functions use fewer passes to save time
    example -->
    stmt='myfunction(30)'
    setup='from __main__ import myfunction'
    """
    import timeit
    t = timeit.Timer(stmt=stmt, setup=setup)
    elapsed = (1000000//passes * t.timeit(number=passes))
    # f string new in Python 3.6
    print(f"{stmt} takes {elapsed:0.3f} microseconds/pass")

def isprime6(n):
    n = abs(n)
    # deal with primes under 5
    if n in (2,3,):
        return True
    # the rest of the primes are multiples of 6 plus or minus 1
    # eliminate 2/3 of the remaining candidates fast
    if (n < 5) or ((n % 6) not in (1, 5,)):
         return False
    # need only try divisors up to sqrt(x) or n**0.5
    for div in range(6, int(round(n**0.5+2)), 6):
        if (n % (div+1) == 0) or (n % (div-1) == 0):
            return False
    return True

# note 9999991 is a prime number, use it for testing
stmt = 'isprime6(9999991)'
setup = 'from __main__ import isprime6'
passes = 1000
use_timeit(stmt, setup, passes)

'''
isprime6(9999991) takes 48.902 microseconds/pass
'''
