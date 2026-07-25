#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Button_style_image_font_tkk2.py

Explore the tkk_Button() and tkk.Style()
Use font and/or an image on the button

Python27+ includes the Tkinter Tile extension Ttk.
Ttk comes with 17 widgets, 11 of which already exist in Tkinter:
Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton,
PanedWindow, Radiobutton, Scale and Scrollbar
The 6 new widget classes are:
Combobox, Notebook, Progressbar, Separator, Sizegrip and Treeview

ttk.Button uses ttk.Style
create a text and an image button
note: newer versions of tkinter allow .png image files

Tuple examples of common fonts
(family, size, weight)
times48b = ('times', 48, 'bold')
times20b = ('times', 20, 'bold')
times12n = ('times', 12, 'normal')
cour20b = ('courier', 20, 'bold')
helv20bi = ('helvetica', 20, 'bold italic')
verd20bi = ('verdana', 20, 'bold italic')
cosa24b = ('Comic Sans MS', 24, 'bold')
helv16b = ('helvetica', 16, 'bold')
# 'normal' is default
arial25n = ['Arial', 25]
calibri10bu = ('calibri', 10, 'bold', 'underline')

docs
https://tkdocs.com/shipman/canvas.html

tested using the Spyder IDE on Linux  vegaseat  19jul2026
'''

import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
# only set size of root
w = 200
h = 160
root.geometry("{}x{}".format(w, h))

cour20b = ('courier', 20, 'bold')

# ttk uses styling for its widgets
style = ttk.Style()
# note that background only forms a yellow outline
style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'yellow')]
    )
# add font info this way
style.configure("C.TButton", font=cour20b)

colored_btn = ttk.Button(text="Text", style="C.TButton")
colored_btn.pack(pady=10)

# create the desired color text with a button image (.gif  .bmp  .png)
#photo = tk.PhotoImage(file='../image/x.png')
# use IrfanView to write the test on a blank image 
photo = tk.PhotoImage(file='/home/admin123/Pictures/image/Button/Btn_yPress1.png')
image_btn = ttk.Button(image=photo, style="C.TButton")
image_btn.pack(pady=10)

root.mainloop()
