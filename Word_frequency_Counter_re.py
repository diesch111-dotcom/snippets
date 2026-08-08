#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Word_frequency_Counter_re.py

Experiments with string processing
Preprocess the string and do a word frequency count

Remove punctuation/whitespace with re
Sort by frequency then word

notice:
the online C compiler on LinuxMint Firefox also runs Python3 
(select Python 3 from dropdown menu in upper left corner)

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

from collections import Counter
import re


def sort_freq_word(tup):
    '''
    helper function for sorting of a list of (word, freq) tuples
    sort by looking at freq tup[1] first then word tup[0]
    the minus sign indicates reverse order sort for freq
    '''
    return (-tup[1], tup[0])


# sample text for testing (could come from any text file)
text = """\
A young executive was leaving the office at 6 pm when he found the CEO
standing in front of a shredder with a piece of paper in hand. "Listen,"
said the CEO, "this is important, and my secretary has left. Can you
make this thing work?"

"Certainly," said the young executive. He turned the machine on,
inserted the paper, and pressed the start button.

To the young executive's surprise the CEO said:
"Excellent, excellent!" as his paper disappeared inside the machine.
"I just need one copy."
"""

# convert text to all lower case
text = text.lower()

# use re to select words (remove punctuations and whitespace)
# \w+ means match 1 or more alphanumeric characters
# returns a list
words = re.findall(r'\w+', text)

# select the 10 most common words
# sorted by fequency (default)
common10 = Counter(words).most_common(10)

print('-'*20)

print("10 most common words sorted by frequency then words in alpha order:")
for word, freq in sorted(common10, key=sort_freq_word):
    print("{:3d}  {}".format(freq, word))


''' result...
10 most common words sorted by frequency then words in alpha order:
 10  the
  3  a
  3  ceo
  3  executive
  3  paper
  3  said
  3  young
  2  he
  2  in
  2  of
'''
