#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' triangular_number.py

counts the objects that can form an equilateral triangle
T0 to T15 gives ...
0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120
or
n*(n + 1)/ 2
see:
http://en.wikipedia.org/wiki/Triangular_number

The triangular number Tn solves the handshake problem of counting the
number of handshakes if each person in a room full of n + 1 total
people shakes hands once with each other person. In other words,
the solution to the handshake problem of n people is Tn-1.

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

def triangular_number(n):
    if n <= 0:
        return 0
    else:
        # uses recursion
        return n + triangular_number(n-1)

info = """\
The triangular number Tn solves the handshake problem of counting the
number of handshakes if each person in a room full of n + 1 total
people shakes hands once with each other person. In other words,
the solution to the handshake problem of n people is Tn-1.
"""
print(info)
# number of objects
n = 15
print("Handshakes (15 people) =", triangular_number(n))

'''
Handshakes (15 people) = 120
'''
