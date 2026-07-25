#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Checkbutton_multi_tk2.py

Exploring multiple Tkinter tk.Checkbutton() widgets
tk.Checkbutton() allows more than one widget to be selected/checked
Click with left mouse button to select or deselect (toggles)
Use a tk.LabelFrame() to give instruction

Here wwe use a choice selection of different fresh fruits

docs
https://tkdocs.com/shipman/checkbutton.html

tested ++ using the Spyder IDE on Linux  vegaseat  19jul2026
'''

import tkinter as tk


def cb_checked():
    # show checked check button item(s)
    label['text'] = ''
    for ix, item in enumerate(cb):
        # 1=checked, 0=unchecked
        if cb_v[ix].get():
            label['text'] += '{} is checked\n'.format(item['text'])


root = tk.Tk()
root['bg'] = 'wheat'
root.title("yummi")

# create a labeled frame for the CheckButtons
# relief='groove' and labelanchor='nw' are default
lbfr = tk.LabelFrame(root, text="  select a fruit  ", bd=3)
lbfr.grid(row=0, column=0, padx=35, pady=10)

fruit_list = [
'apple',
'orange',
'banana',
'pear',
'apricot', 
'plum',
"peach"
]

# list(range()) needed for Python3
cb = list(range(len(fruit_list)))
cb_v = list(range(len(fruit_list)))
for ix, text in enumerate(fruit_list):
    # IntVar() tracks checkbox status (1=checked, 0=unchecked)
    cb_v[ix] = tk.IntVar()
    # command is optional and responds to any cb changes
    cb[ix] = tk.Checkbutton(
        lbfr, 
        text=text,
        variable=cb_v[ix], 
        command=cb_checked)
    cb[ix].grid(row=ix, column=0, sticky='w')

label = tk.Label(root, width=20)
label.grid(row=ix+1, column=0, sticky='w')

# preset check buttons (1=checked, 0=unchecked)
cb_v[1].set(1)
# show initial selection
cb_checked()

root.mainloop()
