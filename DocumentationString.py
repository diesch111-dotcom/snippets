#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' DocumentationString.py

documentation strings must be added right below the function definition,
triple quotes are recommended as a standard
Can be accessed via function_name.__doc__

tested with SublimeText IDE on LinuxMint  vegaseat 15jun2026
'''

def get_distance(x1, y1, x2, y2):
    """
    get_distance(x1, y1, x2, y2)
    returns distance between two points using the pythagorean theorem
    the function parameters are the coordinates of the two points
    """
    dx = x2 - x1
    dy = y2 - y1
    return (dx**2 + dy**2)**0.5

#
# since the indentation rules relax between triple quotes
# you can also use this to avoid adding spaces in front of 
# the doc string
#

def get_distance2(x1, y1, x2, y2):
    """
get_distance(x1, y1, x2, y2)
returns distance between two points using the pythagorean theorem
the function parameters are the coordinates of the two points
    """
    dx = x2 - x1
    dy = y2 - y1
    return (dx**2 + dy**2)**0.5

print( "The function's documentation string:" )
# shows text between the triple quotes
print(get_distance.__doc__)
print("\nWithout leading spaces:")
print(get_distance2.__doc__)

''' result...
The function's documentation string:

    get_distance(x1, y1, x2, y2)
    returns distance between two points using the pythagorean theorem
    the function parameters are the coordinates of the two points
    

Without leading spaces:

get_distance(x1, y1, x2, y2)
returns distance between two points using the pythagorean theorem
the function parameters are the coordinates of the two points
'''
