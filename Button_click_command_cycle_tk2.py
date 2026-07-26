#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Button_click_command_cycle_tk2.py

Click the tk.Button() to cycle through a list of choices.

tested using the Spyder IDE on Linux  vegaseat  19jul2026
"""

import tkinter as tk
from functools import partial
import itertools as itr


def cycle_color(icycle=itr.cycle(['red', 'blue', 'lime', 'tan', 'gold'])):
    '''
    cycles through the given list of colors on each click
    the whole 'itr' object is small enough to be the function argument
    '''
    color = next(icycle)
    #print(color)
    root.title(color)
    root.config(bg=color)

def cycle_text(text_lines_cycle):
    '''
    cycles through the given list of text lines on each click
    text_lines take up space, so use a different approach declaring
    text_lines_cycle = itr.cycle(text_lines) object external and
    passing it in using functools.pertial()
    '''
    text = next(text_lines_cycle)
    #print(text)  # testing...
    label['text'] = text



root = tk.Tk()
root['bg'] = 'tan'

# only set Upper Left Corner ULC (x, y) position of root
root.geometry("+{x}+{y}".format(x=250, y=200))

# humor can be funny...
text_lines = [
    'The first commandment was when Eve told Adam to eat the apple.', 
    'The seventh commandment is thou shalt not admit adultery.', 
    'The epistels were the wives of the apostles.', 
    'It is your money. You paid for it. (GWB)', 
    "Cannibal's recipe book: How to Serve Your Fellow Man."
    ]

text_lines_cycle = itr.cycle(text_lines)
                                 
button1 = tk.Button(
    root, 
    bg= "gold", 
    text="press to cycle colors",
    command=cycle_color)

button2 = tk.Button(
    root, 
    bg= "gold", 
    text="press to cycle lines of text",
    command=partial(cycle_text, text_lines_cycle))

label = tk.Label(root, width=60, font=('times', 14, 'bold'))

# use the pack() layout manager to position the widgets
# default is top down in the center
button1.pack(padx=100, pady=10)
button2.pack(padx=100, pady=10)
label.pack(padx=10, pady=10)

root.mainloop()
