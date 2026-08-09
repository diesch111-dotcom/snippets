#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' slicing_grouper.py

A look at string slicing
slicing can be applied to any Python sequence

[starting-at-index : but-less-than-index [ : step]]
'start' defaults to 0, 'end' to len(sequence), 'step' to 1

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''


def slice_grouper(seq, size=2):
    """
    slice sequence seq into subsequences (groups) of a given size
    return a list of these subsequences
    eg.
    slice_grouper((1, 2, 3, 4, 5)) --> [(1, 2), (3, 4), (5,)]
    slice_grouper("Mississippi", 4)) --> ['Miss', 'issi', 'ppi']
    """
    return [seq[k:k+size] for k in range(0, len(seq), size)]


s4 = "hippopotamus"

print("full string  = %s" % s4)

print("first 2 char = %s" % s4[0:2])
print("next 2 char  = %s" % s4[2:4])
print("last 2 char  = %s" % s4[-2:])
print("exclude first 3 char  = %s" % s4[3: ])
print("exclude last 4 char   = %s" % s4[:-4])
print("reverse the string    = %s" % s4[::-1])
# s4 has not changed
print("the whole word again  = %s" % s4)
# remember [start:end:step]
print("spell skipping 2 char = %s" % s4[::2])


print("playing around = %s%s" % (s4, s4[::-1]))

# use slicing to create a list in groups of 3 char
#mylist = [s4[k:k+3] for k in range(0, len(s4), 3)]
mylist = slice_grouper(s4, 3)
print("slicing into groups of 3 char = %s" % mylist)
# index starts at 0
print("concatinate group 2 and 4 = %s" % (mylist[1] + mylist[3]))

print('-'*36)
print("insert 'ter' 4 places from the end:")
s5 = s4[:-4] + 'ter' + s4[-4:]
print(s5)  # hippopotteramus

'''result ...
full string  = hippopotamus
first 2 char = hi
next 2 char  = pp
last 2 char  = us
exclude first 3 char  = popotamus
exclude last 4 char   = hippopot
reverse the string    = sumatopoppih
the whole word again  = hippopotamus
spell skipping 2 char = hpooau
playing around = hippopotamussumatopoppih
slicing into groups of 3 char = ['hip', 'pop', 'ota', 'mus']
concatinate group 2 and 4 = popmus
------------------------------------
insert 'ter' 4 places from the end:
hippopotteramus
'''

print('-'*36)

# extra
s = "Mississippi"
mylist2 = slice_grouper(s, 4)  # ['Miss', 'issi', 'ppi']
print(mylist2)

print('slice via annotation'.center(30,'-'))

# might be more readable than [::-1]
rev: slice = slice(None, None, -1)
name: str = "Alice"
print(name)
print(name[rev])
print(rev)
print(type(rev))
'''
Alice
ecilA
slice(None, None, -1)
<class 'slice'>
'''
