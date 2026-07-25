#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' LabelFrame_Radiobutton_select_tk2.py

Explore the tk_LabelFrame() container
Use the associated label to give information about usage
Put a number of tk.Radiobutton() widgets in the frame
One can select for instance specific food items
Only one radiobutton can be active at a time, 
however a tk.Checkbutton() allows multple choices

docs
https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/shipman/ttk-Radiobutton.html

Tuple examples of common fonts
(family, size, weight)
times48b = ('times', 48, 'bold')
times20b = ('times', 20, 'bold')
times12n = ('times', 12, 'normal')
cour20b = ('courier', 20, 'bold')
helv20bi = ('helvetica', 20, 'bold italic')
verd20bi = ('verdana', 20, 'bold italic')
cosa24b = ('Comic Sans MS', 24, 'bold')
calibri16b = ("calibri", 16, 'bold')
calibri12bu = ('calibri', 12, 'bold', 'underline')
helv14b = ('helvetica', 14, 'bold')
arial25n = ['Arial' , 25]

tested using the Spyder IDE on Linux  vegaseat  19jul2026
'''

import tkinter as tk

root = tk.Tk()
# only set size of root
w = 400
h = 260
root.geometry("{}x{}".format(w, h))
root.title('tk.LabelFrame() containing tk.RadioButton()')
root['bg'] = 'tan'
# this will change the font in all the root tk widgets (not ttk widgets)
root.option_add('*Font', ("calibri", 14, 'bold'))


def click():
    """shows the value of the radio button selected"""
    s = "{} has been selected".format(vs.get())
    label['text'] = s
    print(s)  # test...


# create a labeled frame for the radiobuttons
# relief='groove' and labelanchor='nw' are default
lbfr = tk.LabelFrame(root, text=" select a food item ", bd=3)
lbfr.pack(padx=35, pady=10)

vs = tk.StringVar(root)
tk.Radiobutton(lbfr, text="egg", value='egg', variable=vs,
    command=click).pack(anchor='w')
tk.Radiobutton(lbfr, text="spam", value='spam', variable=vs,
    command=click).pack(anchor='w')
tk.Radiobutton(lbfr, text="cheese", value='cheese', variable=vs,
    command=click).pack(anchor='w')
tk.Radiobutton(lbfr, text="bacon", value='bacon', variable=vs,
    command=click).pack(anchor='w')
tk.Radiobutton(lbfr, text="mushroom", value='mushroom', variable=vs,
    command=click).pack(anchor='w')
# needed, set initially to None or one of the radiobutton values
#vs.set(None)
vs.set("spam")

label = tk.Label(root)
label.pack(pady=5)
click()

root.mainloop()
