#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' difflib_close_match.py

Match a word to words in a list, adjust quality of match

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

import difflib

word = 'appel'
word_list = ['ape', 'apple', 'peach', 'puppy', 'pork', 'abort']
print(word)
print(word_list)
print('-'*40)

# max number of matches in the returned list (default is 3)
n_max = 6
# value 0 to 1.0 of match quality (default is 0.6)
cutoff = 0.8
print("quality = {}".format(cutoff))
print(difflib.get_close_matches(word, word_list, n_max, cutoff))

print('-'*40)

cutoff = 0.7
print("quality = {}".format(cutoff))
print(difflib.get_close_matches(word, word_list, n_max, cutoff))

print('-'*40)

cutoff = 0.4
print("quality = {}".format(cutoff))
print(difflib.get_close_matches(word, word_list, n_max, cutoff))

""" result...
appel
['ape', 'apple', 'peach', 'puppy', 'pork', 'abort']
----------------------------------------
quality = 0.8
['apple']
----------------------------------------
quality = 0.7
['apple', 'ape']
----------------------------------------
quality = 0.4
['apple', 'ape', 'puppy', 'peach']
"""
