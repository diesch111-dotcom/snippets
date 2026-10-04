#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" with_statement2.py

The convenience of the 'with' statement in file handling

Vegaseat  03oct2026
"""

fname = "CanadaSong.txt"

data = """\
First come the black flies,
Then the Horse flies,
Then the Deer flies,
Then the snow flies!
"""

# 'with' will close the file handle properly
# "w" will create a new file if it does not exist
# otherwise it will overwrite the existing file
# "a" will append to an existing file
with open(fname, "w") as fout:
    fout.write(data)

print("{} has been written".format(fname))

print('-'*40)

# "r" and read() gives a string of the existing file data
with open(fname, "r") as fin:
    text = fin.read()

print(text)
'''
First come the black flies,
Then the Horse flies,
Then the Deer flies,
Then the snow flies!
'''