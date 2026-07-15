''' Combobox_pasta_ttk3.py

Exploring the Tkinter expansion module ttk.Combobox(),
also show the options.

Python27+ includes the Tkinter Tile extension module ttk.
Ttk comes with 17 widgets, 11 of which already exist in Tkinter:
Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton,
PanedWindow, Radiobutton, Scale and Scrollbar
The 6 new widget classes are:
Combobox, Notebook, Progressbar, Separator, Sizegrip and Treeview

docs
https://tkdocs.com/shipman/
https://tkdocs.com/shipman/ttk-Combobox.html
Maybe helpfull for planing your next dinner!

tested using the Spyder IDE on Linux  dns aka vegaseat  13jul2026
'''

import tkinter as tk
import tkinter.ttk as ttk


def selection_changed(event):
    """a combo box item has been selected, show the item"""
    s = "You selected {}".format(combo.get())
    root.title(s)

pasta_list = [
'Spaghetti',
'Vermicelli',
'Bucatini',
'Fettuccine',
'Linguine',
'Lasagne',
'Cavatappi',
'Manicotti',
'Macaroni',
'Maultaschen',
'Penne',
'Rigatoni',
'Ziti',
'Farfalle',
'Flaedle',
'Spatzen',
'Orzo'
]

root = tk.Tk()
w = 380
h = 250
x = 100
y = 70
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("{}x{}+{}+{}".format(w, h, x, y))
# use a tkinter named color
root['bg'] = 'wheat'
root.title('Select a pasta from the combo box')

# sort the pasta list first
pasta_list = sorted(pasta_list)
# one way to load the combobox is via values
# width is text width, height is lines of text
combo = ttk.Combobox(root, 
                     width=20, 
                     height=10, 
                     values=pasta_list)
# position the combobox with absolute coordinates
combo.place(x=10, y=10)
# bind selection to an action
combo.bind('<<ComboboxSelected>>', selection_changed)

# another way to load the combo box with the pasta list
#combo['values'] = pasta_list

# set the initial pasta
combo.set(pasta_list[0])

# shows possible options for the ttk.Cobobox() widget
import pprint
pprint.pprint(combo.keys())

root.mainloop()

''' possible options for ttk.Cobobox() ...
['height',
 'postcommand',
 'values',
 'exportselection',
 'font',
 'invalidcommand',
 'justify',
 'show',
 'state',
 'textvariable',
 'validate',
 'validatecommand',
 'width',
 'xscrollcommand',
 'foreground',
 'background',
 'takefocus',
 'cursor',
 'style',
 'class']
'''
