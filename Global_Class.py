#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Global_Class.py

Using a class to give all global variables a 'safe' namespace


tested using the Spyder IDE on Linux  dns(vegaseat)  11jul2026
"""

# a class to the rescue, to give all global variables a namespace
class GlobalClass(object):
    """declare all global variables here"""
    x = 0
    z = False

# now all global variables get a namespace (the class instance)
# use something like 'ww' (from WorldWide) for a recognizable 
# namespace 'ww.' for global variables
ww = GlobalClass()

def incr_wwx() :
    """ww.x changes, but does not have to be declared global"""
    ww.x += 1
    return ww.x

# testing...
print(incr_wwx())  # 1
print(incr_wwx())  # 2
print(incr_wwx())  # 3

print(ww.x)  # 3
print(ww.z)  # False

#print(globals())
print("="*40)
#print(vars())

# curious...
[print(k) for k, v in globals().items() if k.startswith("ww")]
