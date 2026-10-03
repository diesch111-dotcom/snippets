#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' yield_from_make_list2.py

"yield from" is new in Python 3.3
Use it to create a list via a range generator

VegasEat  21sep2026
'''

def range_gen(n):
    '''
    generate a complex list...
    for item in iterable: yield item 
    is simplified to:
    with yield from iterable
    '''
    yield from range(-n, 0)
    #yield from range(1, n+1)
    yield from range(n*20, n*40, 20)
    #yield from list('abc')  # or...
    yield from {'a': 1, 'b': 2, 'c': 3}
    


# testing ...
print("Create a complex list:")
mylist = list(range_gen(5))
print(mylist)

'''
Create a complex list:
[-5, -4, -3, -2, -1, 100, 120, 140, 160, 180, 'a', 'b', 'c']
'''
