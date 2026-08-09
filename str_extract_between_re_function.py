#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' str_extract_between_re_function.py

Extract the text between two substrings using Python module re
Uses first occurrence of substring1 and last occurrence of substring2
Extract is case sensitive

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

import re

def extract_re(text, sub1, sub2):
    """
    use regex to extract a substring from text between two
    substrings sub1 (first occurrence) and sub2 (last occurrence)
    arguments are case sensitive
    """
    pattern = re.compile(
        "%s(.*)%s" % (re.escape(sub1), re.escape(sub2)), re.DOTALL
    )
    match = pattern.search(text)
    if match:
        #print(match, match.group(0), match.group(1))  # test
        return match.group(1)
 
    
text = "The quick brown fox jumps over the lazy dog."
print(repr(extract_re(text, 'The', 'fox')))

print('-'*50)

text2 = '''\
The quick brown fox jumps over this lazy dog. The rather sly fox 
laughed at the stupid dog.    
'''
print(repr(extract_re(text2, 'The', 'fox')))
print('-'*50)
# picks up the 'the' from 'rather'
# add a space after 'the' to make it stand alone
print(repr(extract_re(text2, 'the', 'fox')))

'''
' quick brown '
--------------------------------------------------
' quick brown fox jumps over this lazy dog. The rather sly '
--------------------------------------------------
'r sly '
'''
