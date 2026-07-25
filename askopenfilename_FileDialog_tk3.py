#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' askopenfilename_FileDialog_tk3.py

Here we make the 'initialdir' the working directory to be more generic.
Single click a filename to select it.
Click the upper right side 'green' symbol to go to folders 'above', then
double click those folders to open them up to show their filenames.

Tkinter's filedialogs...
to get a directory, get a filename or file handle
tkfd.askdirectory(**options) returns directory name
after the directory has been selected use....
tkfd.askopenfilename(**options) returns file name
tkfd.askopenfilenames(**options) returns selected file names
tkfd.askopenfile(**options) returns file handle to load from
tkfd.asksaveasfile(**options) returns file handle to save to
tkfd.asksaveasfilename(**options) returns file name to save to

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
full_path = tkfd.askopenfilename(initialdir=basedir, filetypes=mask)
# testing...
print("Selected: {}".format(full_path))
# extract just the filename
filename = os.path.basename(full_path)
# testing...
print("Selected: {}".format(filename))

"""
# use current directory, get only .txt files
mask = [("Text files","*.txt")]
filename = tkfd.askopenfilename(filetypes=mask)

print("Selected textfile = {}".format(filename))

#filehandle = tkfd.askopenfile(filetypes=mask)
"""

''' possible result...

Selected: /home/admin123/AAtest_py/tk_ttk/askstring_simpledialog_tk2.py
Selected: askstring_simpledialog_tk2.py

'''

# optional help
#help(tkfd)
