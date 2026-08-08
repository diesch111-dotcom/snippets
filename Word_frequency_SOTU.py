#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Word_frequency_SOTU.py

Experiments with string processing
Preprocess the string and do a word frequency count
Words with matching frequency are in alphabetical reverse order

Analyse a number of State of the Union (SOTU) speeches...
https://time.com/5777857/state-of-the-union-transcript-2020/

eg.
StateOfTheUnion2020.txt  Donald Trump
StateOfTheUnion2010.txt  Barak Obama
StateOfTheUnion2002.txt  George Bush

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

from string import punctuation
from collections import Counter

print('''"StateOfTheUnion2020.txt" (Donald Trump) ...
result (50 most common words) ...''')

fname = "/home/admin123/AAtest_py/data/StateOfTheUnion2020.txt"
# sample text for testing (could come from any text file)
# UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 10908
# to fix this use "utf-8" encoding
with open(fname, encoding="utf-8") as fin:
    dt_text = fin.read()

# since "nation's" would turn into "nations", optionally remove 's
dt_text2 = dt_text.replace("'s", "")

# remove punctuation marks and change to lower case
dt_text3 = ''.join(c for c in dt_text2.lower() if c not in punctuation)

# dt_text3.split() splits at white spaces
# use a generator expression to generate a list of (freq, word) tuples
cnt = ((f, w) for w, f in Counter(dt_text3.split()).items())
# use reverse sort to show highest frequency first
for f, w in sorted(cnt, reverse=True)[:50]:
    print("{:3d}  {}".format(f, w))

'''
"StateOfTheUnion2020.txt" (Donald Trump) ...
result (50 most common words) ...

291  the
196  and
161  to
150  of
107  in
 99  is
 92  a
 91  our
 88  we
 66  are
 63  for
 62  that
 54  i
 52  have
 39  you
 38  —
 37  with
 35  on
 34  this
 34  american
 32  will
 27  was
 27  my
 26  has
 25  new
 25  as
 24  states
 24  his
 23  be
 23  at
 23  america
 23  all
 22  than
 22  not
 22  also
 21  united
 21  people
 20  one
 20  by
 19  he
 19  administration
 18  first
 18  country
 17  years
 17  their
 17  now
 17  more
 17  america’s
 16  your
 16  just

'''
