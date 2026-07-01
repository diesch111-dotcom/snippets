#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" import101.py

the 'import' keyword is how you bring code from external files, 
modules, or packages into your current script

Python looks in a very specific order defined by a list of paths called 
sys.path.

shorten the name
import module as alias

prefix 'module.' not needed
from module import func1, func2

can cause "namespace pollution" so avoid this
wildcard import everything in module
from module import *

Python looks here for import:
The Current Directory: The folder where your running script lives.
PYTHONPATH: An optional environment variable containing directories 
    you've specified.
Standard Library Directories: Built-in Python modules (like os, math, sys).
Site-Packages (Third-Party): Where tools installed via pip (like requests 
                             or django) live.

If you are building a larger project, you will want to import code 
    across your own files.


works with LinuxMint and Spyder IDE  dns(vegaseat)  15jun2026
"""

print("Python looks here for import:")
import sys
for path in sys.path:
    print(path)

# line of 40 '='
print("="*40)

# shorten the name
import numpy as np
import collections as coll

# Instead of numpy.array(), you write:
my_array = np.array([1, 2, 3])

str_seq = "mississippi"
# Counter(iterable) is a dict subclass for counting hashable items
# elements are stored as dictionary keys and their counts as dictionary values
ctr = coll.Counter(str_seq)
print(str_seq)
print('list of keys:')
print(ctr.keys())
print('list of values:')
print(ctr.values())
print('list of items:')
print(ctr.items())
# .most_common(n) list the n most common elements and their counts 
# If n is None, then list all element counts, sorted by count 
print("most common:")
print(ctr.most_common()) # [('i', 4), ('s', 4), ('p', 2), ('m', 1)]
print("as dictionary:")
print(dict(ctr.most_common())) # {'i': 4, 's': 4, 'p': 2, 'm': 1}
print("how many 'i' = ctr['i']:")
print(ctr['i'])  # 4

print("="*40)

# no 'math.' prefix needed for sqrt and pi
from math import sqrt, pi

print(pi)       # 3.141592653589793 (No "math." prefix needed)
print(sqrt(25)) # 5.0

# using __import__
t = lambda: __import__('time').localtime()
print('Date (d/m/yyyy): %s/%s/%s'%(t().tm_mday, t().tm_mon, t().tm_year))

''' possible result -->
Date (d/m/yyyy): 25/6/2026
'''

# tkinter is the standard GUI (Graphical User Interface) library for Python.
# ttk is the Tkinter Tile extension that comes with 17more  widgets like:
# Combobox, Notebook, Progressbar, Separator, Sizegrip and Treeview

import tkinter as tk
import tkinter.ttk as ttk


def selection_changed(event):
    """a combo box item has been selected, show the item"""
    s = "You selected {}".format(combo.get())
    root.title(s)

pasta_list = [
'Spaghetti',
'Vermicelli',
'Bucatini',
'Fettuccine',
'Linguine',
'Lasagne',
'Cavatappi',
'Manicotti',
'Macaroni',
'Penne',
'Rigatoni',
'Ziti',
'Farfalle',
'Flaedle',
'Spatzen',
'Orzo'
]

root = tk.Tk()
w = 380
h = 250
x = 100
y = 70
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("{}x{}+{}+{}".format(w, h, x, y))
# use a tkinter named color
root['bg'] = 'wheat'
root.title('Select a pasta from the combo box')

# sort the pasta list
pasta_list = sorted(pasta_list)
# one way to load the combobox via values
# width is text width, height is lines of text
combo = ttk.Combobox(root, width=20, height=10, values=pasta_list)
# position the combobox
combo.place(x=10, y=10)
# bind selection to an action
combo.bind('<<ComboboxSelected>>', selection_changed)

# another way to load the combo box with the pasta list
#combo['values'] = pasta_list

# set the initial pasta
combo.set(pasta_list[0])

root.mainloop()



