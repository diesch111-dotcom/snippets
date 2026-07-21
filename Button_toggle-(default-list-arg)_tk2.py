#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' button_toggle-(default-list-arg)_tk1.py

Make a toggle button with Tkinter using a static variable

docs
https://tkdocs.com/shipman/entry.html
https://tkdocs.com/shipman/button.html

tested with LinuxMint and Spyder IDE  vegaseat  20jul2026
'''

import tkinter as tk


def entryColor(tog=[0]):
    '''
    toggle the entry color between white and red
    the default list argument forms a static variable
    '''
    # toggles between True and False
    tog[0] = not tog[0]
    if tog[0]:
        edit1.config(bg='red')
    else:
        edit1.config(bg='lime')


root = tk.Tk()
# create a button, command runs the given function ref
# when button is clicked
btn1 = tk.Button(root, text="Toggle Color", command=entryColor)
btn1.pack(fill=tk.BOTH, expand=1)

# us a font to make entry() widget taller
times48b = ('times', 48, 'bold')
# create an entry box to color
edit1 = tk.Entry(root, font=times48b, bg='tan', width=10)
edit1.pack(fill=tk.BOTH, expand=1)

root.mainloop()
