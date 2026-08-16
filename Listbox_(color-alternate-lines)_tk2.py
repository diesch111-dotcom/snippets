#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Listbox_(color-alternate-lines)_tk2.py

Load a Tkinter Listbox with data
color alternate lines
and select a listbox item with the mouse

colors:
Tkinter can use a number of named color strings (not case sensitive) like
red, green, blue, white, black, tan, pink, yellow, magenta, lightblue
lightgreen, moccasin, peachpuff, orange, grey, purple, brown ...

docs
https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/shipman/

tested with Spyder IDE on LinuxMint  VegasEat 16aug2026
'''

import tkinter as tk
    

def get_selection(event=None):
    """
    function to read the listbox selection
    and put the result in a label widget
    """
    # get selected line index
    index = listbox.curselection()[0]
    # get the line's text
    seltext = listbox.get(index)
    # put the selected text in the label
    label['text'] = seltext
    

# the main window
root = tk.Tk()
# only set ULC (x, y) position of root
root.geometry(f"+{60}+{150}")
root.title("tk.Listbox")

# create a label (width in characters)
# text will display centered (default)
label = tk.Label(root, width=15, bg="lime")

# create a listbox (height in characters)
listbox = tk.Listbox(root, height=15)

friend_list = [
'Stew', 'Tom', 'Jens', 'Oliver', 'Ali', 'Ethel',
'Barb', 'Tabia', 'Tim', 'Pete', 'Sue', 'Zambina',
'Frank', 'Gisela', 'Theo', 'Morgan', 'Mia']

# load the listbox withe sorted list
for index, item in enumerate(sorted(friend_list)):
    listbox.insert('end', item)
    # optionally color alternate lines
    if index % 2:
        listbox.itemconfig(index, bg='light blue')
    
# left mouse click on a list item to display selection
listbox.bind('<ButtonRelease-1>', get_selection)
# use mouse wheel to scroll listbox items, focus first
listbox.focus()

# pack() the widgets from center top down (default)
listbox.pack(padx=5)
label.pack()

root.mainloop()
