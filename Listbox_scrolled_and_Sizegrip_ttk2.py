#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Listbox_scrolled_and_Sizegrip_ttk2.py

Explore a tk.Listbox having a vertical ttk.Scrollbar
Also tests the ttk.Sizegrip to stretch the window

https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/shipman/

tested using the SublimeText IDE on LinuxMint  vegaseat  4jul2026
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
       

root = tk.Tk()
# only set ULC (x, y) position of root
root.geometry(f"+{60}+{150}")
root.title("IC assortment from Walmart ")
# this will change the font in all the root widgets
root.option_add('*Font', ("Helvetica", 22))

#times12n = ('times', 12, 'normal')

# tk's StringVar() will update the result_label automatically
result_var = tk.StringVar()
result_label = tk.Label(textvariable=result_var, fg='red')

listbox = tk.Listbox(height=8, bg='beige', width=68)
listbox.grid(column=0, row=0, sticky='nwes')

scroll = ttk.Scrollbar(command=listbox.yview, orient='vertical')
listbox['yscrollcommand'] = scroll.set
scroll.grid(column=1, row=0, sticky="ns")

result_label.grid(column=0, row=1, sticky='we')

sz = ttk.Sizegrip()
sz.grid(column=1, row=1, sticky='se')

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# use left mouse click on a list item to display selection
listbox.bind('<ButtonRelease-1>', on_click_listbox)

IC_list = ['PC817c DIP-4, general-purpose photocopier',
 'ICL7660 ultra-voltage converter, charge pump',
 'NE555 DIP-8, timer, pulse generation, oscillator',
 'LM358 DIP-8, low power bi-power amplifier',
 'LM324 DIP-14, four working amplifiers',
 'JRC4558 DIP-8, double working amplifier',
 'LM393 DIP-14, low offset voltage dual comparator',
 'LM339 DIP-8, low-power four-voltage comparator',
 'NE553 2 DIP-8, dual high-performance low-noise operational amplifiers',
 'LM386m DIP-8, low power audio frequency amplifier',
 'TDA2030A TO-220, audio amplifier in pentawatt package',
 'TDA2822D DIP-8, low power stereo amplifier',
 'PT2399 DIP-16, CMOS Echo audio processor',
 'UC3842AN DIP-8, high-performance current controller',
 'UC3843AN DIP-8, high-performance current controller',
 'ULN2003AN DIP-16, bipolar (BJT) transistor array 7 NPN Darlington 50V 500mA',
 'ULN2803APG DIP-18, bipolar (BJT) transistor array 8 NPN Darlington 50V 500mA']

# fill the Listbox
for ic in IC_list:
    listbox.insert('end', ic)

root.mainloop()
