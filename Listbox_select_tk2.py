''' Listbox_select_tk2.py

Get the value of a selected item from a Tkinter tk.Listbox()

https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/shipman/label.html
https://tkdocs.com/shipman/button.html
https://tkdocs.com/shipman/listbox.html


tested using the Spyder IDE on Linux  dns aka vegaseat  13jul2026
'''

import tkinter as tk
from tkinter import ttk  # for ttk.Sizegrip()


def on_click_listbox(event=None):
    # get selected line index
    index = listbox.curselection()
    # get the line's text
    seltext = listbox.get(index)
    # will update the result_label automatically
    # by setting StringVar result_var
    result_var.set(seltext)    


root = tk.Tk()

# tk's StringVar() will update the result_label automatically
result_var = tk.StringVar()
result_label = tk.Label(textvariable=result_var, width=20)

listbox = tk.Listbox(root, width=20, height=7)

mylist = ['green', 'blue', 'red', 'gold', 'pink', 'black']
# load the listbox
for color in mylist:
    listbox.insert('end', color)

# layout manager, stack widget vertically
listbox.pack()
result_label.pack()

# use left mouse click on a list item to display selection
listbox.bind('<ButtonRelease-1>', on_click_listbox)

# test
data = listbox.get(0, 'end')  # all the listbox items
print(data)
'''
('green', 'blue', 'red', 'gold', 'pink', 'black')
'''

sz = ttk.Sizegrip()
sz.pack(anchor='se')

# show options
print(listbox.keys())

root.mainloop()
