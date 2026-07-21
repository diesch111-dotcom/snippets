#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Spinbox_ttk2.py

Test the ttk.Spinbox() action
has an area for showing the current value and a pair of arrowheads
click the arrowheads to change the values up or down
ttk.Spinbox() has been available since Python 3.7

from_= minimum value
to= maximum value
wrap=True (once max/min value is reached starts at min/max again)
values can be set to a tuple of discrete steps
otherwise steps=1 from min to max
command=function to show value changes

docs
https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/shipman/spinbox.html
https://tkdocs.com/shipman/label.html
https://tkdocs.com/shipman/colors.html


Python27+ includes the Tkinter Tile extension Ttk.
Ttk comes with 17 widgets, 11 of which already exist in Tkinter:
Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton,
PanedWindow, Radiobutton, Spinbox, Scale and Scrollbar
The 6 new widget classes are:
Combobox, Notebook, Progressbar, Separator, Sizegrip and Treeview

tested with LinuxMint and Spyder IDE   vegaseat  17jul2026
'''

import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('300x200')
#root.resizable(False, False)
root.title('ttk.Spinbox() wrap=True')

def value1_changed():
    '''
    value1.get() is a string
    so is spin_box1.get()
    '''
    sf = "spin_box1 value = {}"
    print(sf.format(value1.get()))
    # or use spin_box1.get()
    print(type(spin_box1.get()))

def value2_changed():
    '''
    value2.get() is a string
    so is spin_box2.get()
    '''
    sf = "spin_box2 value = {}"
    print(sf.format(value2.get()))
    # or use spin_box2.get()


myfont = ('courier', 20, 'bold')

value1 = tk.StringVar(value=0)
# ttk.Spinbox() from 0 to 30 in steps of 1 (default)
# Python already has keyword 'from' so 'from_' is used
# size adjusts to font
spin_box1 = ttk.Spinbox(
    root,
    from_=0,
    to=30,
    increment=1,
    font=myfont,
    textvariable=value1,
    wrap=True,
    foreground='red',
    command=value1_changed)
# you can use a pack dictionary
# side='left' centers heightwise
pack_dict = {'side': 'top', 'padx': 5, 'pady': 5}
spin_box1.pack(**pack_dict)
#spin_box1.pack()

value2 = tk.StringVar(value=30)
# ttk.Spinbox() with discrete steps given in values
# size adjust to font or you can give width in letters
spin_box2 = ttk.Spinbox(
    root,
    from_=10,
    to=60,
    values=(10, 20, 30, 40, 50, 60),
    textvariable=value2,
    wrap=True,
    width=30,
    command=value2_changed)
# use the the pack dictionary from spin_box1   
spin_box2.pack(**pack_dict)
#spin_box2.pack()

# shows possible options for the ttk.Spinbox() widget
# background does not work
import pprint
pprint.pprint(spin_box1.keys())

root.mainloop()

'''
['values',
 'from',
 'to',
 'increment',
 'format',
 'command',
 'wrap',
 'exportselection',
 'font',
 'invalidcommand',
 'justify',
 'show',
 'state',
 'textvariable',
 'validate',
 'validatecommand',
 'width',
 'xscrollcommand',
 'foreground',
 'background',
 'takefocus',
 'cursor',
 'style',
 'class']
'''