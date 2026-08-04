#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' deque_rotate.py

Working with deque (double ended que, pronounced 'deck')
Rotate n positions to the right or left

tested with SublimeText IDE on LinuxMint  vegaseat 15jun2026
'''

from collections import deque

mylist = [1, 2, 3, 4, 5, 6, 7]
print(mylist)
print('convert a list to a deque:')
mydeque = deque(mylist)
print(mydeque)
print(type(mydeque))

print('rotate 3 positions to the right with +3:')
mydeque.rotate(3)

print(mydeque)

print('rotate 3 positions to the left again with -3:')
mydeque.rotate(-3)
print(mydeque)

print('convert a deque to a list:')
print(list(mydeque))

'''
[1, 2, 3, 4, 5, 6, 7]
convert a list to a deque:
deque([1, 2, 3, 4, 5, 6, 7])
<class 'collections.deque'>
rotate 3 positions to the right with +3:
deque([5, 6, 7, 1, 2, 3, 4])
rotate 3 positions to the left again with -3:
deque([1, 2, 3, 4, 5, 6, 7])
convert a deque to a list:
[1, 2, 3, 4, 5, 6, 7]
'''

