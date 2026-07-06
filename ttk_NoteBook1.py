#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" ttk_NoteBook1.py

exploring the Tkinter expansion module ttk.Notebook()

ttk comes with 17 widgets, 11 of which already exist in Tkinter:
Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton,
PanedWindow, Radiobutton, Scale and Scrollbar

The 6 new widget classes are:
Combobox, Notebook, Progressbar, Separator, Sizegrip and Treeview

docs
https://tkdocs.com/shipman/ttk-Notebook.html
https://tkdocs.com/shipman/listbox.html
https://tkdocs.com/shipman/label.html
https://tkdocs.com/shipman/button.html
https://tkdocs.com/shipman/frame.html

using the Spyder IDE on Linux  dns(vegaseat) 4jul2026
"""

import tkinter as tk
import tkinter.ttk as ttk


def listbox1_select(event=None):
    # get selected line index
    index = listbox1.curselection()
    # get the line's text
    seltext = listbox1.get(index)
    str = f"Selected pasta item:\n {seltext}"
    if seltext == "Spaetzle":
        str += " ... Mahlzeit!"
    label1.config(text=str)
    print(str)  # testing
    
def listbox2_select(event=None):
    # get selected line index
    index = listbox2.curselection()
    # get the line's text
    seltext = listbox2.get(index)
    # unpaack it
    gas, percent = seltext 
    str = f"The earth athmosphere contains\n {percent} {gas}"
    label2.config(text=str)
    print(str)  # testing
    
def listbox3_select(event=None):
    # get selected line index
    index = listbox3.curselection()
    # get the line's text
    seltext = listbox3.get(index)
    # unpack it
    element, percent = seltext
    str = f"The earth crust contains\n {percent} {element}"
    label3.config(text=str)
    print(str)  # testing
     
    
# just a few found on my 'Mahlzeit' table
pasta_list = [
'Spaghetti','Vermicelli','Bucatini','Fettuccine','Linguine','Lasagne',
'Cavatappi','Manicotti','Macaroni','Penne','Rigatoni','Ziti','Farfalle',
'Orzo','Spaetzle','Maultaschen','Knoepfle','Fingernudel']

# air makeup
gases_list = [\
 ['Nitrogen', '78.084%'], ['Oxygen', '20.946%'], ['Argon', '0.934%'],
 ['Neon', '0.002%'], ['Helium', '5.24ppm'], ['Krypton', '1.14ppm'],
 ['Hydrogen', '0.50ppm'], ['Xenon', '0.09ppm'], ['CO2', '0.033%'],
 ['CH4', '2ppm']]

earth_elements_list = [\
 ['Oxygen', '46.40%'], ['Silicon', '28.20%'], ['Aluminum', '8.32%'],
 ['Iron', '5.63%'], ['Calcium', '4.15%'], ['Sodium', '2.36%'],
 ['Magnesium', '2.33%'], ['Potassium', '2.09%'], ['Titanium', '0.57%'],
 ['Hydrogen', '0.14%'], ['Phosphorus', '0.11%'], ['Manganese', '0.09%'],
 ['Fluorine', '0.06%'], ['Barium', '0.06%'], ['Strontium', '0.04%'],
 ['Sulfur', '0.03%'], ['Carbon', '0.02%'], ['Zirconium', '0.02%'],
 ['Vanadium', '0.01%'], ['Chlorine', '0.01%'], ['Chromium', '0.01%']]

# need a window to place widgets into
root = tk.Tk()
# set the root window's width, height and x,y position
# x,y are the upper left corner ULC coordinates 
# in pixels
w = 540
h = 200
x = 50
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry(f"{w}x{h}+{x}+{y}")
root.title("exploring the tkinter ttk.Notebook() widget")
# give the root some color, default is a grey white
root.configure(bg="wheat")

nbk = ttk.Notebook(root)

# create a child frame for each page of the notebook
page1 = tk.Frame(bg='red')
page2 = tk.Frame(bg='blue')
page3 = tk.Frame(bg='green')

# create the pages, text goes on the page tabs
nbk.add(page1, text='Pasta')
nbk.add(page2, text='Athmosphere')
nbk.add(page3, text='Earth Crust')

listbox1 = tk.Listbox(page1, bg='yellow')
for item in sorted(pasta_list):
    listbox1.insert('end', item)
# use left mouse click on a list item to get/display selection
listbox1.bind('<ButtonRelease-1>', listbox1_select)
label1 = tk.Label(page1, text="You seleted:", font=['Arial', 18])

listbox2 = tk.Listbox(page2, bg='yellow')
for item in sorted(gases_list):
    listbox2.insert('end', item)
# use left mouse click on a list item to get/display selection
listbox2.bind('<ButtonRelease-1>', listbox2_select)
label2 = tk.Label(page2, text="You seleted:", font=['Arial', 16])

listbox3 = tk.Listbox(page3, bg='yellow')
for item in sorted(earth_elements_list):
    listbox3.insert('end', item)
# use left mouse click on a list item to get/display selection
listbox3.bind('<ButtonRelease-1>', listbox3_select)
label3 = tk.Label(page3, text="You seleted:", font=['Arial', 16])

# using the pack() layout manager 
# took me a while to get it straight
nbk.pack(fill='both', expand='yes')
listbox1.pack(side='left', anchor='nw', padx=8, pady=5)
listbox2.pack(side='left', anchor='nw', padx=8, pady=5)
listbox3.pack(side='left', anchor='nw', padx=8, pady=5)
label1.pack(pady=5)
label2.pack(pady=5)
label3.pack(pady=5)

root.mainloop()

