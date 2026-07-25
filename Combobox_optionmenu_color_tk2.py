#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Vombobox_optionmenu_color_tk2.py

Using tk.Optionmenu() as a combobox
Check the Tkinter expansion module's ttk.Combobox()

tested using the Spyder IDE on Linux  vegaseat  4jul2026
'''

import tkinter as tk


def select(event):
    sf = "selected: {}".format(var.get())
    root.title(sf)
    # optional, set root window background to selected color
    color = var.get()
    root['bg'] = color


root = tk.Tk()
# set the root window's height, width and x,y position
# x,y are the upper left corner coordinates in pixels
w = 330
h = 200
x = 50
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("{}x{}+{}+{}".format(w, h, x, y))
root.title("tk.Optionmenu() as combobox")

var = tk.StringVar(root)
# initial value
var.set('white')

lbl = tk.Label(root, text='select a color')
# side='left' centers the y axis , widgets are side by side
lbl.pack(side='left', padx=10)

# pick from the predefined named tkinter colors
choices = ['red1', 'red2', 'red3', 'red4', 'green', 'lime', 'blue', 
           'aqua', 'azure', 'lightblue', 'yellow', 'gold', 'orange', 
           'white', 'pink', 'magenta', 'gainsboro', 'beige', 'bisque', 
           'moccasin', 'tan', 'brown', 'thistle', 'plum', 'purple']
# the * unpacks the list          
option = tk.OptionMenu(root, var, *choices, command=select)
option.pack(side='left', padx=10)

root.mainloop()
