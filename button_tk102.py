#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" button_tk102.py

A button is one of the most fundamental tkinter GUI widgets. It’s used 
to trigger an action (some Python function) when a user clicks on it.

creating a tk.Button(parent, options...)
some options are...
text: a string displayed on the button.
command: name of the function to execute when clicked, no ()
bg/fg: background color and foreground color of text. 
    accepts color names like "red" or hex strings like "#ff0000".
state: can be set to tk.NORMAL (default) or tk.DISABLE
font: a tuple defining the font (family, size, and weight)
    (e.g., ("Helvetica", 12, "bold")
padx/pady: internal padding of text in pixels

here we use the
Tkinter grid() layout manager: (need to experiment with this) 
The size of a grid cell in a given row or column is
determined by its largest widget.

If you give a grid layout more space than it needs,
it will fill this space from its center on out.
A way around this is to use place() with a frame and
then grid() within this frame.

can use layout manager grid() and layout manager place(x, y) together
where place(x, y) positions absolute using x and y coordinates

Check out the same idea with a pack() layout manager in 'button_tk101.py'

docs
https://tkdocs.com/shipman/button.html
https://tkdocs.com/shipman/grid.html
https://tkdocs.com/shipman/colors.html

some info from Google Gemini
 
tested with LinuxMint and Spyder IDE  dns(vegaseat)  4jul2026

"""

import tkinter as tk


def button_click():
    " action when button is clicked  "
    # change the label text
    label.config(text="Button Clicked!")
    
def greet(name):
    " this function expects an argument 'name' "
    # test
    #print(f"Hello, {name}!")
    # change the label text
    label.config(text=f"Hello, {name}!")


# main application window/root
root = tk.Tk()
root.title("tk.Button example")
# set the root window's width, height and x,y position
# x,y are the upper left corner ULC coordinates 
# in pixels
w = 450
h = 220
x = 50
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry(f"{w}x{h}+{x}+{y}")
# default is 'white'
root.configure(bg="wheat")

# create a label to show the action, font is optional
# a label is there to show text
label = tk.Label(
    root, 
    text="Click the button below", 
    font=("Arial", 12, "bold"),  # font is optional, but nice
    fg="white",   # foreground color of text
    bg="black",   # background color of label
    padx=10,      # padding around text
    pady=5
)

# create the Button
# the 'command' argument tells Tkinter which function to run when clicked
button = tk.Button(
    root, 
    text="Click Me", 
    command=button_click,  # don't use functions ()
    bg="green",            # background color
    fg="white",            # foreground color eg. white text
    font=("Arial", 10, "bold"),  # font is optional, but nice
    padx=10,               # internal horizontal padding
    pady=5                 # internal vertical paddingin 
)

# Use lambda so the argument is passedto function greet when clicked
button2 = tk.Button(
    root, 
    text="Greet", 
    command=lambda: greet("Norbert"),
    bg="gold",            # background color
)

# change button color when pressed
btn1 = tk.Button(root, text='Heidi', activebackground='cyan',
        bg='yellow', command=lambda: greet("Heidi")) 

# change button color when pressed
btn2 = tk.Button(root, text='Helga', activebackground='cyan',
        bg='green', fg='white',command=lambda: greet("Helga"))

# change button color when pressed
btn3 = tk.Button(root, text='Hilde', activebackground='lime',
        bg='blue', fg='white', command=lambda: greet("Hilde"))

# position the widgeta using the grid(row, column) layout manager
# rows and columns start at 0
# use sticky=tk.E+tk.W or sticky='ew' to expand full East to West
#label.grid(row=0, column=0, columnspan=3, sticky='ew')
label.grid(row=0, column=3, pady=5, columnspan=1, sticky='ew')
button.grid(row=1, column=3)
button2.grid(row=2, column=3, pady=5)
# all of column 0 follows padx             
btn1.grid(row=3, column=0, padx=5) 
btn2.grid(row=3, column=1, padx=5) 
btn3.grid(row=3, column=2) 

# root.destroy is safe way to exit mainloop
quit_button = tk.Button(root, text=" Quit!", command=root.destroy)

# the odd ball position
# place into Lower Right Corner (LRC)
quit_button.place(x=w-80, y=h-40)

# start the application loop
root.mainloop()

