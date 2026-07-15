#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Button_Label_Style_ttk1.py

A look at foreground/background colors of 
ttk.Button()
ttk.Label()
using ttk.Style() and ttk.Style().configure()

Trick: Use a ttk.Label or tk.Label right on top of the ttk.Button
to get a properly colored text.

Or one could simply use a button with a message_image created with an
image editor.

docs
https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/shipman/ttk-style-layer.html
https://tkdocs.com/shipman/ttk-Button.html


tested using the Spyder IDE on Linux  dns aka vegaseat  13jul2026
'''

import tkinter as tk
import tkinter.ttk as ttk


def click_ttk_btn():
    root.title('ttk_btn clicked')
    
def pressed1(event):
    root.title('label on button has been pressed')
    
def pressed2(event):
    root.title('image_btn has been pressed')


root = tk.Tk()
# only set size of root
w = 360
h = 260
root.geometry("{}x{}".format(w, h))
root['bg'] = 'green'
root.title('Using ttk.Style()')

# typical tk button
tk_btn = tk.Button(
    root, 
    text="tk_Button", 
    bg='blue', 
    fg='yellow')
# now color a ttk button with styling (bg/fg like in tk_btn won't do)
# foreground color works, but background color is just an outline
ttk.Style().configure("RB.TButton", foreground='blue', background='yellow')
ttk_btn = ttk.Button(
    root, 
    text="ttk_Button", 
    style="RB.TButton",
    command=click_ttk_btn)
# foreground/background works with a ttk.Label but not a ttk.Button
# the way you expect
# to get around this you can top the ttk button with a label
style = ttk.Style()
# now style the label
style.configure("GB.TLabel", foreground="white", background="red")
ttk_label = ttk.Label(
    root, 
    text="ttk_Label",
    style="GB.TLabel")
# use a label instead of button text for proper colors
# then put the label right on top of the ttk button
ttk.Style().configure("LB.TButton", foreground='red', background='yellow')
ttk_btn2 = ttk.Button(
    root, 
    text="", 
    style="LB.TButton")
# style the label
ttk.Style().configure("LB.TLabel", foreground="red", background="yellow")
# put the label right on top of the ttk_btn
ttk_label2 = ttk.Label(
    ttk_btn2, 
    text="press me", 
    style="LB.TLabel")
# this label hides the button, so bind it for any action
ttk_label2.bind('<Button-1>', pressed1)
# create the desired color text with a button image (.gif  .bmp  .png)
# using an image editor
#photo = tk.PhotoImage(file='../image/x.png')
photo = tk.PhotoImage(file='../image/png/Btn_yPress1.png')
image_btn = ttk.Button(image=photo, style="C.TButton")
image_btn.bind('<Button-1>', pressed2)

tk_btn.pack(pady=10)
ttk_btn.pack(pady=10)
ttk_label.pack(pady=10)
ttk_btn2.pack(pady=10)
ttk_label2.pack(padx=4, pady=4)
image_btn.pack(pady=10)

root.mainloop()
