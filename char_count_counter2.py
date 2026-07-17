#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' char_count_counter2.py

Using collections.Counter() to count characters in a string/text.
The neat way to go about.

English literature 12 most common letter frequency order is:
e  t  a  o  i  n  s  h  r  d  l  u

tested using Linux and Spyder IDE  vegaseat  17jul2026
'''

import collections
import string


# has all lower case ASCII letters
alpha_lower = string.ascii_lowercase

text = """"\
I want to die in my sleep like grandpa. 
Not yelling and screaming like the passengers in his car!
"""

# preprocess text to only contain lower case letters
str2 = "".join(c for c in text.lower() if c in alpha_lower)

print(text)

# list of (char, freqency) tuples, default order is high frequency first
count = collections.Counter(str2).most_common()

print(count)

print("All letters in lower case, high frequency first:")
for letter, freq in count:
    print("'{}'  {}".format(letter, freq))

''' result...
All letters in lower case, high frequency first:
'e'  10
'i'  9
'n'  9
'a'  7
's'  6
'l'  5
't'  4
'g'  4
'r'  4
'd'  3
'p'  3
'o'  2
'm'  2
'y'  2
'k'  2
'c'  2
'h'  2
'w'  1
'''
