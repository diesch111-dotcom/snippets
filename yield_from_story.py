#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" yield_from_story.py

Something to wrap your mind around.
Need to complete your Python 102 lecture.

VegasEat  03oct2026
"""

def range_gen(s):
    '''
    generate a complex list...
    for item in iterable: yield item 
    is simplified to:
    yield from iterable
    '''
    yield from 'The '
    yield from s[0:5] + ' and the '
    yield from s[5:] + ' went to lunch at '
    yield from s[::-1][0:7]

    
s = "hippopotamus"
story_list = list(range_gen(s))

# join the list to form a sentence
print("".join((c for c in story_list)))

'''
The hippo and the potamus went to lunch at sumatop
'''

