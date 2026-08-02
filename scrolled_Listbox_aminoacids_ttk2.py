#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" scrolled_Listbox_aminoacids_ttk2.py

For names and images of common aminoacids see 
http://en.wikipedia.org/wiki/Alanine etc.

Also tests ttk.Sizegrip to stretch the window

tested using the SublimeText IDE on Linux  vegaseat  4jul2026
"""

import tkinter as tk
import tkinter.ttk as ttk
    
    
def on_click_listbox(event=None):
    # get selected line index
    index = listbox.curselection()
    # get the line's text
    seltext = listbox.get(index)
    # will update the result_label automatically
    # by setting StringVar result_var
    result_var.set(seltext)
    file_name = aminoacid_png_dict[seltext]
    print(file_name)
       

root = tk.Tk()

# Tk's StringVar() will update the result_label automatically
result_var = tk.StringVar()
result_label = tk.Label(textvariable=result_var, width=20)

listbox = tk.Listbox(height=5)
listbox.grid(column=0, row=0, sticky='nwes', padx=10)
# add the scrollbar
scroll = ttk.Scrollbar(command=listbox.yview, orient='vertical')
listbox['yscrollcommand'] = scroll.set
scroll.grid(column=1, row=0, sticky="ns")

result_label.grid(column=0, row=1, sticky='we', padx=10)

sz = ttk.Sizegrip()
sz.grid(column=1, row=1, sticky='se')

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# use left mouse click on a list item to display selection
listbox.bind('<ButtonRelease-1>', on_click_listbox)

# name: file_name dictionary of common amino acids
aminoacid_png_dict = \
{'alanine': '../image/Aminoacids/L-Alanine.png',
 'arginine': '../image/Aminoacids/L-Arginine.png',
 'asparagine': '../image/Aminoacids/L-Asparagine.png',
 'aspartic_acid': '../image/Aminoacids/L-Aspartic acid.png',
 'cysteine': '../image/Aminoacids/L-Cysteine.png',
 'glutamic_acid': '../image/Aminoacids/L-Glutamic acid.png',
 'glutamine': '../image/Aminoacids/L-Glutamine.png',
 'glycine': '../image/Aminoacids/Glycine.png',
 'histidine': '../image/Aminoacids/L-Histidine.png',
 'isoleucine': '../image/Aminoacids/L-Isoleucine.png',
 'leucine': '../image/Aminoacids/L-Leucine.png',
 'lysine': '../image/Aminoacids/L-Lysine.png',
 'methionine': '../image/Aminoacids/L-Methionine.png',
 'phenylalanine': '../image/Aminoacids/L-Phenylalanine.png',
 'proline': '../image/Aminoacids/L-Proline.png',
 'serine': '../image/Aminoacids/L-Serine.png',
 'threonine': '../image/Aminoacids/L-Threonine.png',
 'tryptophan': '../image/Aminoacids/L-Tryptophan.png',
 'tyrosine': '../image/Aminoacids/L-Tyrosine.png',
 'valine': '../image/Aminoacids/L-Valine.png'}

# fill the Listbox
aminoacid_list = aminoacid_png_dict.keys()
file_list = aminoacid_png_dict.values()
for aminoacid in aminoacid_list:
    listbox.insert('end', aminoacid)

root.mainloop()
