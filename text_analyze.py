#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' text_analyze.py

A simple way to analyze text

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

text = '''\
A dad is on his way home a bit late from the office when he realizes
that it's his daughter's birthday and he has not bought her a gift.
So he stops at a toy store to buy his daughter a Barbie doll.  Inside
the store he sees a Barbie display and asks the salesgirl how much the
dolls are.

The salesgirl responds:
"Oh, we have
Gymnasium Barbie at $19.95
Volleyball Barbie at $19.95
Shopping Barbie at $19.95
Surfer Barbie at $19.95
Disco Barbie at $19.95
and Divorced Barbie at $299.99!"

Shocked, the man asks, "Why is Divorced Barbie $299.95 when all the other
Barbies are $19.95?"

The salesgirl responds:
"Sir, Divorced Barbie comes with:
Ken's Car
Ken's House
Ken's Boat
Ken's Furniture
Ken's Jewelery
Ken's Money
Ken's Computer
and Ken's Best Friend.!"'''

print("Number of lines in text  = {}".format(text.count('\n'))) # newline
word_list = text.split()
print("Number of words in text  = {}".format(len(word_list)))
print("Number of spaces in text = {}".format(text.count(" ")))
print("Number of characters     = {}".format(len(text)))

''' result...
Number of lines in text  = 27
Number of words in text  = 133
Number of spaces in text = 109
Number of characters     = 758
'''
