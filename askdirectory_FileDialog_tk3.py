#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' askdirectory_FileDialog_tk3.py

This code will start at the working direcory as 'initialdir' to be more generic
then you can use the upper right side 'green' symbol to work back levels

double click the directory selected
further double clicks will bring up any subdirectories
single click gets the specfied initialdir

Use Tkinter's filedialog...
to get a directory, get a filename or file handle
tkfd.askdirectory(**options) returns directory name
after the directory has been selected use...
tkfd.askopenfilename(**options) returns file name
tkfd.askopenfilenames(**options) returns selected file names
tkfd.askopenfile(**options) returns file handle to load from
tkfd.asksaveasfile(**options) returns file handle to save to

https://docs.python.org/3/library/tkinter.html
https://docs.python.org/3/library/dialog.html#module-tkinter.filedialog

tested using the Spyder IDE on Linux  vegaseat  19jul2026
'''

import tkinter as tk
import tkinter.filedialog as tkfd
import os
# get working directory
basedir = os.getcwd()

# use the 2 lines below for inclusion into programs
# that have their own eventloop like Pygame
root = tk.Tk()
root.withdraw()

# default is working directory as initial dir
#dirname = tkfd.askdirectory()
dirname = tkfd.askdirectory(initialdir=basedir, 
                            title="select a directory")

print(dirname)

''' possible result...
/home/admin123/AAtest_py/tk_ttk
/home/admin123/AAtest_py/Chemistry
/home/admin123/AAtest_py
'''

# optional help
#help(tkfd.askdirectory)