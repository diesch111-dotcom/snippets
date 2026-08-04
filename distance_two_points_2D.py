#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' distance_two_points_2D.py

Calculate the distance between two points given the coordinates
of the points (x1, y1) and (x2, y2) in a 2D space

next:
do this in a 3D space

tested with SublimeText IDE on LinuxMint  vegaseat 15jun2026
'''

import math


def get_distance(x1, y1, x2, y2):
    '''
    returns distance between two points using the pythagorean theorem
    the function parameters are the 2D coordinates of the two points
    '''
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx**2 + dy**2)


sf = "Distance between point({}, {}) and point({}, {}) is {:.3f}"

x1, y1 = 1, 3
x2, y2 = 4, 7
print(sf.format(x1, y1, x2, y2, get_distance(x1, y1, x2, y2)))

x3, y3 = 2, 5
x4, y4 = 11, 23
print(sf.format(x3, y3, x4, y4, get_distance(x3, y3, x4, y4)))

'''
Distance between point(1, 3) and point(4, 7) is 5.000
Distance between point(2, 5) and point(11, 23) is 20.125
'''