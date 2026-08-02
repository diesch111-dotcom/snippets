#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' decorator_stripchar.py

Using a Python class as a decorator
A decorator class to strip given chrs from string text
by default strips common punctuation marks = ,.?!:;$

tested with SublimeText IDE on LinuxMint   vegaseat  15jun2026
'''

class StripCharacters:
    """
    a decorator class to strip given chrs from string text
    by default strip common punctuation marks = ,.?!:;$
    """
    def __init__(self, func, chrs=",.?!:;$"):
        self.chrs = chrs
        self.func = func
        
    def __call__(self, text):
        """
        allows the class instance to be called as a function
        """
        # do the stripping
        new_text = ''.join(c for c in text if c not in self.chrs)
        return self.func(new_text)


# notice how the decorator is applied to the function
@StripCharacters
def print_text(text):
    print(text)
    
text1 = 'If you are here, you are lost!  Pay $5.00 for help.'
print_text(text1)

print('-'*30)

text2 = 'common punctuation marks are ,.?!:;'
print_text(text2)

''' result...
If you are here you are lost  Pay 500 for help
------------------------------
common punctuation marks are 
'''
