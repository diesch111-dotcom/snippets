#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" pi_approximate_Ramanujan.py

Some functions which give an approximation
of the famous irrational number pi (π)
The approximation by Ramanujan is very good!

Srinivasa Ramanujan (1887–1920) was an Indian mathematician

tested with Spyder IDE on LinuxMint  vegaseat 15jun2026
"""

from math import factorial
from decimal import Decimal, getcontext


def pi_riemann(n_max, digits=50):
    """
    Riemann's algorithm to calculate
    pi (π) coverges slowly so
    uses module decimal
    """
    getcontext().prec = digits
    pi = 0
    k = 1
    while k <= n_max:
        pi += Decimal(1)/k**2
        k += 1
    return (6 * pi).sqrt()


def pi_euler(n_max, digits=50):
    """
    Euler's algorithm to calculate pi
    (π) converges slowly
    uses module decimal
    """
    getcontext().prec = digits
    pi = 0
    k = 1
    while k <= n_max:
        pi += Decimal(1)/k**4
        k += 1
    return (90*pi).sqrt().sqrt()


def pi_ramanujan(n_max, digits=50):
    """
    Ramanujan's algorithm to calculate
    pi (π) that converged extremely fast
    2 iterations are actually good enough!
    uses Python module decimal
    """
    getcontext().prec = digits
    pi = 0
    k = 0
    while k <= n_max:
        pi += (Decimal(factorial(4*k))/Decimal(factorial(k)**4))*\
            Decimal((1103 + 26390*k))/Decimal((4*99)**(4*k))
        k += 1
    return 9801/(2*Decimal(2).sqrt()*pi)


if __name__ == "__main__":
    # testing...
    print("50 digits published pi:")
    print("3.1415926535897932384626433832795028841971693993751")
    print("pi_ramanujan(6):")
    print(pi_ramanujan(6))
    print("pi_riemann(100):")
    print(pi_riemann(100))
    print("pi_euler(100):")
    print(pi_euler(100))

    ''' result...
50 digits published pi:
3.1415926535897932384626433832795028841971693993751
pi_ramanujan(6):
3.1415926535897932384626433832795028841971693993751
pi_riemann(100):
3.1320765318091059044445112609662110476408802241920
pi_euler(100):
3.1415924153073680619056438548725969359226080339811
    '''