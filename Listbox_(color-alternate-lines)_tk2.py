''' Listbox_(color-alternate-lines)_tk2.py

Load a Tkinter tk.Listbox() with data then
color alternate lines and select a listbox item with a mouse click.

docs
https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/shipman/listbox.html


tested using the Spyder IDE on Linux  dns aka vegaseat  15jul2026
'''

import tkinter as tk
    

def get_list(event=None):
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
    root.title(seltext)
    

# the main window
root = tk.Tk()

# create a label (width in characters)
label = tk.Label(root, width=15)
label.pack()

# create a listbox (height in characters)
listbox = tk.Listbox(root, height=15)
listbox.pack()

friend_list = [
'Stew', 'Tom', 'Jens', 'Adam', 'Al', 'Ethel',
'Barb', 'Tiny', 'Tim', 'Pete', 'Sue', 'Zack',
'Frank', 'Gustav', 'Ted', 'Morgan', 'Karen']

# load the listbox
for index, item in enumerate(friend_list):
    listbox.insert('end', item)
    # optionally color alternate lines
    if index % 2:
        listbox.itemconfig(index, bg='light blue')
    
# left mouse click on a list item to display selection
listbox.bind('<ButtonRelease-1>', get_list)
# use mouse wheel to scroll listbox items, focus first
listbox.focus()

root.mainloop()
