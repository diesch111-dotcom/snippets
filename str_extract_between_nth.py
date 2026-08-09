#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' str_extract_between_nth.py

Extract the text between two substrings using Python's split function
Can apply nth occurrence of substring1 and nth occurrence of substring2
Extraction is case sensitive

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

def extract_between(text, sub1, sub2, nth=1):
    """
    extract a substring from text between two given substrings
    sub1 (nth occurrence) and sub2 (nth occurrence)
    arguments are case sensitive
    """
    # prevent sub2 from being ignored if it's not there
    if sub2 not in text.split(sub1, nth)[-1]:
        return None
    return text.split(sub1, nth)[-1].split(sub2, nth)[0]


text = "The quick brown fox jumps over the lazy dog."

print(repr(extract_between(text, 'The', 'fox')))
print('-'*20)
# there is no 'fox' after lower case 'the'
print(repr(extract_between(text, 'the', 'fox')))

'''
' quick brown '
--------------------
None
'''

print('='*20)

# test nth occurrence of substrings
text2 = '''\
The quick brown fox jumps over the lazy dog. The rather sly fox 
laughed at the stupid dog.    
'''

# check the second occurrence, nth=2
print(repr(extract_between(text2, 'The', 'fox', nth=2)))
print('-'*20)
# picks up the 'the' from 'rather'
# add a space after 'the' to make it stand alone
print(repr(extract_between(text2, 'the', 'fox', nth=2)))

'''
' rather sly '
--------------------
'r sly '
'''
