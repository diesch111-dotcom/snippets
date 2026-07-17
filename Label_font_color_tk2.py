#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Label_font_color_tk2.py

Explore Tkinter's tk.Label() widget fonts, background and text colors
Tinter takes color names or hex strings like "#ff0000" = 'red'

doc
https://tkdocs.com/shipman/label.html
https://tkdocs.com/shipman/fonts.html

use tkinter.colorchooser.askcolor() to get hex strings

Examples of common font tuples assigned to variable names:
(family, size, weight)
times48b = ('times', 48, 'bold')
times20b = ('times', 20, 'bold')
times12n = ('times', 12, 'normal')
cour20b = ('courier', 20, 'bold')
helv20bi = ('helvetica', 20, 'bold italic')
verd20bi = ('verdana', 20, 'bold italic')
cosa24b = ('Comic Sans MS', 24, 'bold')
helv16b = ('helvetica', 16, 'bold')
arial25n = ['Arial' , 25]
'normal' is the default
Linux will pick work_alikes if possible

tested with LinuxMint and Spyder IDE  dns aka vegaseat  4jul2026
'''

import pprint
import tkinter as tk
import tkinter.font as tkf

# create mainwindow
root = tk.Tk()
# set the root window's width, height and x,y position
# x,y are the upper left corner ULC coordinates 
# in pixels
w = 450
h = 100
x = 50
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry(f"{w}x{h}+{x}+{y}")

mytext = " Hello, world! "

times48b = ('times', 48, 'bold')
cosa48b = ('Comic Sans MS', 48, 'bold')
cosa48bi = ('Comic Sans MS', 48, 'bold italic')
cour48bi = ('courier', 48, 'bold italic')
# select one of the above font tuple
myfont = ('Comic Sans MS', 48, 'bold italic')
# or variable name
#myfont = cosa48bi

# create a label showing mytext using myfont
# red characters on yellow background
label = tk.Label(root, text=mytext, font=myfont, fg='red', bg='yellow')
# position the label
label.pack(pady=10)

root.title(myfont)

# BTW:
# setting up the font with tkf.Font() has some advantages
# the instance of tkf.Font() can yield interesting information
# using  .measure()   .cget()   .actual()
new_font = tkf.Font(family="Arial", size=48, weight="bold")
# get pixel width of a text in a given font, handy info
s3 = 'how are you today'
print('Pixel width of string "{}" = {}'.format(s3, new_font.measure(s3)))
print(new_font.cget('family'))
print(new_font.cget('slant'))
print('show the new_font dictionary:')
pprint.pprint(new_font.actual())

'''
note: 'Liberation Sans' is the actual work_alike on LinuxMint

Pixel width of string "how are you today" = 564
Arial
roman
show the new_font dictionary:
{'family': 'Liberation Sans',
 'overstrike': 0,
 'size': 48,
 'slant': 'roman',
 'underline': 0,
 'weight': 'bold'}
'''

# start the event loop
root.mainloop()
