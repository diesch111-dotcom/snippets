#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" search_codefile2.py

A handy snippet to quickly search all the .py code files in a
directory/folder for a segment of code. Just put this little 
ik utility into a folder and run it.  I use it a lot!

btw: I love to eat out in LV hence the name vegas eat

using the Spyder IDE on Linux  dns aka vegaseat 7jul2026
"""

import glob
import os

# code segment ...
#search = "with"
search = ".after"

# use current working directory to look at all python code files
# change  "*.py" to "*.txt" to look at all the .txt text files etc.
directory = os.path.join(os.getcwd(), "*.py")

path_list = []

for path in glob.glob(directory):
    #print(path)  # testing,,,
    path_list.append(path)

# do the search
for path in sorted(path_list):
    dirname, fname = os.path.split(path)
    linenum = 0
    with open(path, errors="ignore") as fin:
        code = fin.read()
        for line in code.split('\n'):
            linenum += 1
            if search in line:
                print('"{}" in line {} of {}'.format(search, linenum, fname))
