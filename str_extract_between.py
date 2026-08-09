#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' str_extract_between.py

Etract the text between two substrings using str.partition()
Uses first occurrence of substring1 and first occurrence of substring2
Extract is case sensitive

str.partition(sep) plit str at the first occurrence of sep, return a 3-tuple
  containing the part before, the separator itself, and the part after

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

def extract_between(text, sub1, sub2):
    """
    extract a substring from text between two given substrings
    sub1 (first occurrence) and sub2 (first occurrence)
    arguments are case sensitive
    """
    # prevent sub2 from being ignored if it's not there
    if sub2 not in text.partition(sub1)[-1]:
            return None
    return text.partition(sub1)[2].partition(sub2)[0]
    

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

print("="*52)

# more
text2 ='Advice is easier to give than to receive.'
print(text2.partition('to'))
print(repr(extract_between(text2, 'to', 'to')))

'''
('Advice is easier ', 'to', ' give than to receive.')
' give than '
'''

print("="*25)

# str.partition(sep) -> tuple
print("123.456.78".partition('.'))  # ('123', '.', '456.78')

cost = "$123,456.78"
# str.rpartition(sep) -> tuple
print(cost.rpartition('.'))  # ('$123,456', '.', '78')

print("="*25)

dollars, sep, cents = "123,456.78".rpartition('.')
# take care of $ char too
mydollars = float(dollars.replace(',', '').lstrip('$'))
print('dollars =', mydollars)
mycents = int(cents)
print('cents =', mycents)
print('total = ', mydollars + mycents/100)

'''
dollars = 123456.0
cents = 78
total = $ 123456.78
'''
