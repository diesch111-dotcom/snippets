#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Listbox_sort_tk2.py

Load a Tkinter Listbox with data,
then button click to sort the data

docs
https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/shipman/

tested with Spyder IDE on LinuxMint  VegasEat 16aug2026
'''

import tkinter as tk


def sort_listbox(event):
    # convert the tuple to a list for sorting
    data = list(listbox.get(0, 'end'))
    print(data)
    # delete contents of present listbox
    listbox.delete(0, 'end')
    # load listbox with sorted data
    for item in sorted(data):
        listbox.insert('end', item)
    sort_btn['text'] = "List has ben sorted"


# the main window
root = tk.Tk()
# only set ULC (x, y) position of root
root.geometry(f"+{60}+{150}")
root.title("sort the listbox items")

# create a button to click for sorting
sort_btn = tk.Button(text="Click to sort listbox")
sort_btn.bind("<Button-1>", sort_listbox)

# create a listbox (height in characters)
listbox = tk.Listbox(root, height=15, bg='yellow')
listbox.pack()

friend_list = [
'Steve', 'Tom', 'Mark', 'Olivia', 'Alison', 'Ethel', 'Penny',
'Barb', 'Otto', 'Mia', 'Pete', 'Sue', 'Zambina', 'Lance']

# load the listbox
for item in friend_list:
    listbox.insert('end', item)
 
# pack() widgets  from top down center (default)
sort_btn.pack(pady=5)    
listbox.pack(padx=5)   
    
root.mainloop()
