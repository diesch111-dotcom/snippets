#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Word_frequency_Counter.py

Experiments with string processing
Preprocess the string and do a word frequency count
Words with matching frequency show in reverse alphabetical order

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

from string import punctuation
from collections import Counter

text2 = '''\
A woman goes into labor at a very modern hospital.  The doctor says,
we have a new pain transfer device that can let the father take some
of the pain away from the mother, but I have to warn you even 10% is
pretty bad on a man.

The husband says, I have a high pain threshold let me have it.

The doctor sets the machine at 10% and the husband says, that's not
bad give me 25%. He takes that and says go ahead up to 50%. No problem
go to 75%, not bad go to 100% The baby is born and the doctor tells
the husband that is twice what any other husband has endured, it would
kill most men.

The man goes home and finds the mailman, dead on the front porch.
'''

# remove punctuation marks and change to lower case
text3 = ''.join(c for c in text2.lower() if c not in punctuation)

# text3.split() splits text3 at white spaces
# use a generator expression to generate a list of (freq, word) tuples
cnt = ((f, w) for w, f in Counter(text3.split()).items())
# use reverse to show highest frequency first
for f, w in sorted(cnt, reverse=True)[:10]:
    print("{:3d}  {}".format(f, w))

''' result ...
 14  the
  5  a
  4  to
  4  says
  4  husband
  4  have
  4  and
  3  that
  3  pain
  3  is
'''
