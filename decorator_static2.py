#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' decorator_static2.py

Create a decorator to make certain variables of a decorated 
function static (retain value), similar to C++

vegaseat  15oct2026
'''

def static_vars(**kwargs):
    """
    a decorator to create static variables within a decorated function
    """
    def inner(func):
        func.__dict__.update(kwargs)
        return func
    return inner


@static_vars(a=0, b=1)
def my_func(x):
    my_func.a += x
    my_func.b *= x
    return my_func.a, my_func.b


# testing...
print(my_func(1))  # (1, 1)
print(my_func(1))  # (2, 1)
print(my_func(1))  # (3, 1)

print(my_func(7))  # (10, 7)
print(my_func(7))  # (17, 49)
