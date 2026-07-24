#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''' Combobox_files_ttk2.py

Exploring the Tkinter expansion module ttk.Combobox()

Load the Combobox with a file list via glob.glob() and show selection

Python27+ includes the Tkinter Tile extension Ttk.
Ttk comes with 17 widgets, 11 of which already exist in Tkinter:
Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton,
PanedWindow, Radiobutton, Scale and Scrollbar
The 6 new widget classes are:
Combobox, Notebook, Progressbar, Separator, Sizegrip and Treeview

docs
https://tkdocs.com/shipman/
https://tkdocs.com/shipman/ttk-Combobox.html
https://tkdocs.com/shipman/optionmenu.html
https://docs.python.org/3/library/tkinter.html

tested with LinuxMint and Spyder IDE   vegaseat  17jul2026
'''

import glob
import os
import tkinter as tk
#import tkinter.font as tkFont
import tkinter.ttk as ttk


def selection_changed(event):
    """
    a combo box item has been selected, show the item in window title
    """
    s = "Selected:  {}".format(combo.get())
    root.title(s)

def make_filelist(directory, ext1='*.csv', ext2='*.txt'):
    """
    create a list of files of a given directory having given extensions
    use defaults if no extensions are given
    """
    os.chdir(directory)
    file_list = glob.glob(ext1) + glob.glob(ext2)
    return file_list


root = tk.Tk()
# window geometry is width x height + x_offset + y_offset
root.geometry("440x120+320+200")
root.title('Select a file from the combo box')
root['bg'] = 'tan'

# supply the directory of interest 
file_list = make_filelist("/media/admin123/9325-9047/AAtest_py/tk_ttk")

# width is in characters
combo = ttk.Combobox(root, width=50)
# position the combobox
combo.place(x=10, y=10)
# bind selection to an action
combo.bind('<<ComboboxSelected>>', selection_changed)

# load the combo box with the file list
combo['values'] = file_list

# set the initial file
combo.set(file_list[0])

root.mainloop()
