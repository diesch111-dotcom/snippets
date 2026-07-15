#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Listbox_multiselect_cheese_tk1.py

Create a scrollable listbox using Tkinter's tk.Listbox()
Load the listbox with tasty cheese data,
then select your favorite cheese or cheeses with the mouse by
pressing <Shift> and/or <Ctrl> to select multiple cheeses.

https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/shipman/


tested using the Spyder IDE on Linux  dns aka vegaseat  13jul2026
'''

import tkinter as tk
import tkinter.scrolledtext as tkst


def get_list(event):
    """
    function to read the listbox selection(s)
    and put the result in a tkst.ScrolledText() widget
    """ 
    indices = listbox.curselection()
    print(indices, len(indices))  # test
    # do we have multiselected line indices
    if len(indices) > 1:
        # get the selected lines text
        seltext = '\n'.join(listbox.get(ix) for ix in indices)
    else:
        seltext = listbox.get(indices) + '\n'
    edit_space.insert('insert',seltext)
    print(seltext)  # test


root = tk.Tk()
root.title("Cheeses to Taste")
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("230x480+100+70")
root['bg'] = 'beige'

sf = """\
Click on a cheese
press <Shift> and/or
<Ctrl> for multiples\
"""
# create a label (width in characters)
label_info = tk.Label(root, text=sf, width=25, fg='blue')
label_info.grid(row=0, column=0, pady=5)

edit_space = tkst.ScrolledText(
    master = root,
    wrap   = 'word',  # wrap text at full words only
    width  = 25,      # in characters
    height = 5,       # text lines
    bg='wheat'        # background color of edit area/space
)
# the padx/pady space will form a border effect
edit_space.grid(row=2, column=0, pady=5)

myfont = times12n = ('times', 12, 'normal')
result_var = tk.StringVar()
print(result_var)

# create a listbox (height in characters/lines)
# give it a nice yellow background (bg) color
# press <Shift> and/or <Ctrl> to select multiple listelements
listbox = tk.Listbox(root, height=15, font=myfont, bg='yellow', 
                width=25, selectmode='extended', listvariable=tk.StringVar)
listbox.grid(row=1, column=0)

# the Tkinter listbox does not automatically scroll, you need
# to create a vertical scrollbar to the right of the listbox
yscroll = tk.Scrollbar(command=listbox.yview, orient=tk.VERTICAL)
yscroll.grid(row=1, column=1, sticky='n'+'s')
listbox.configure(yscrollcommand=yscroll.set)

cheese_list = [
'Feta', 'Limburger', 'Camembert', 'Roquefort', 'Edam',
'Romadur', 'Liptauer', 'Dubliner', 'Gouda', 'Gorgonzola',
'Jarlsberg', 'Golka', 'Garrotxa', 'Swiss', 'Quesillo',
'Emmentaler', 'Appenzeller', 'Raclette', 'Asiago', 'Zuvi',
'Ricotta', 'Mozzarella', 'Munster', 'Parmesan', 'Cheddar',
'Blue Stilton', 'Cheshire', 'Wensleydale']

# load the listbox
for item in cheese_list:
    listbox.insert('end', item)

# use left mouse click on a list item to display selection
listbox.bind('<ButtonRelease-1>', get_list)

#print(listbox.keys())

root.mainloop()
