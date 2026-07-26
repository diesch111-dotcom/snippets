#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' asksaveasfile_FileDialog_tk3.py

Make the 'initialdir' the working directory to be more generic.
Make the defaultextension=".py" or maybe an image file ".png"

The Tkinter filedialog for saving a file
tkfd.asksaveasfile(**options) returns file handle to save to.
If file exists, it asks if 'overwrite' is wanted!  If 'No' you can 
change the name, eg. add a 'b' or '2' in the dialog window.

docs
https://docs.python.org/3/library/dialog.html#module-tkinter.filedialog

tested using the Spyder IDE on Linux  vegaseat  19jul2026
'''

import tkinter as tk
import tkinter.filedialog as tkfd
import os
# get working directory
basedir = os.getcwd()

# use the 2 lines below for inclusion into programs
# that have their own event-loop like Pygame
root = tk.Tk()
root.withdraw()

mask = [
    ("Python files","*.py"),
    ('Portable Network Graphics', '*.png'),
    ("JPEG files","*.jpg"),
    ("GIF files","*.gif"),
    ("Text files","*.txt"),
    ("All files","*.*")
    ]

# if the filename does not have an extension
# it will add the specified defaultextension
file_save = "test_code77"
fout = tkfd.asksaveasfile(
    title="Save to a file, defaultextension='.py'",
    initialdir=basedir,
    initialfile=file_save,
    defaultextension=".py",
    filetypes=mask)

# test write a file
data = """\
Men should be tall and handsome.  If you are the typical out of 
shape mouse potato that is standard fare in computer departments, 
you have to make up for your deficiency with money, sports car 
and/or alcohol.
"""
fout.write(data)
# close filehandle properly!
fout.close()

# testing...
print(fout, end='\n\n')
print(fout.name)

'''  possible result...

<_io.TextIOWrapper name='/home/admin123/Documents/test_code77.py' 
mode='w' encoding='UTF-8'>

/home/admin123/Documents/test_code77.py

'''
