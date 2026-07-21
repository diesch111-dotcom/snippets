#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Button_style_ttk2.py

Explore the tkk_Button() and tkk.Style() with style.configure().
Add style to all ttk.Buttons()
Add common font to all tk widgets (not ttk widgets)

Python27+ includes the Tkinter Tile extension Ttk.
Ttk comes with 17 widgets, 11 of which already exist in Tkinter:
Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton,
PanedWindow, Radiobutton, Scale and Scrollbar
The 6 new widget classes are:
Combobox, Notebook, Progressbar, Separator, Sizegrip and Treeview

Tuple examples of common fonts:
(family, size, weight)
times48b = ('times', 48, 'bold')
times20b = ('times', 20, 'bold')
times12n = ('times', 12, 'normal')
cour20b = ('courier', 20, 'bold')
helv20bi = ('helvetica', 20, 'bold italic')
verd20bi = ('verdana', 20, 'bold italic')
cosa24b = ('Comic Sans MS', 24, 'bold')
helv16b = ('helvetica', 16, 'bold')
# 'normal' is default
arial25n = ['Arial', 25]
calibri12bu = ('calibri', 12, 'bold', 'underline')

docs
https://www.geeksforgeeks.org/python-add-style-to-tkinter-button/
https://tkdocs.com/shipman/ttk-Button.html
https://tkdocs.com/shipman/ttk-style-layer.html
https://tkdocs.com/shipman/ttk-theme-layer.html
https://tkdocs.com/shipman/colors.html


tested using the Spyder IDE on Linux  dns aka vegaseat  13jul2026
'''

import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root['bg'] = 'aqua'
# only set size of root
w = 400
h = 220
root.geometry("{}x{}".format(w, h))
root.title("tkk_Button() and tkk.Style()")

# this will change the font in all the root tk widgets (not ttk widgets)
#root.option_add('*Font', ("Helvetica", 20))
root.option_add('*Font', ("calibri", 20, 'bold', 'underline'))

style = ttk.Style()

cosa20b = ('Comic Sans MS', 20, 'bold')
# will add style to every available ttk button
# even though we are not passing style to every button widget
# put font here
style.configure('TButton', foreground='red', font=cosa20b)

# this quit works, exits program
btn1 = ttk.Button(
    root, 
    text='Quit!', 
    style='TButton', 
    command=root.destroy)
# button 2
btn2 = ttk.Button(
    root, 
    text='button2', 
    command=None)
# button3 is a tk button, should not have style but has common font
btn3 = tk.Button(
    root, 
    text='button3', 
    command=None)

# position all the widgets using grid() layout
btn1.grid(row=0, column=3, padx=100, pady=10)
btn2.grid(row=1, column=3, pady=10, padx=100)
btn3.grid(row=2, column=3, pady=10, padx=100)

root.mainloop()
