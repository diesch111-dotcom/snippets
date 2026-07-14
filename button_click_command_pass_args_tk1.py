''' button_click_command_pass_args_tk1.py

A Tkinter example showing several ways for command to 'pass' an argument
('command=' accepts a function reference not a function call)


tested using the Spyder IDE on Linux  vegaseat aka Joe's Dad  13jul2026
'''

import tkinter as tk
from functools import partial
import itertools as itr


# use a typical closure, function within a funtion ...
def closure_callback(val):
    def closure():
        root.title(val)
    # return to inner function    
    return closure

# lambda has done the work for you as the outer function ...
def change_title(val):
    "val via lambda function"
    root.title(val)

def on_Button4(val):
    """
    val argument passed via a partial function, nice and clean
    """
    root.title(val)

def change_color(icycle=itr.cycle(['red', 'blue', 'lime', 'tan', 'gold'])):
    '''
    cycles through the given list of colors on each click
    '''
    color = next(icycle)
    #print(color)
    root.title(color)
    root.config(bg=color)
    

root = tk.Tk()
root['bg'] = 'tan'

# only set Upper Left Corner ULC (x, y) position of root
root.geometry("+{x}+{y}".format(x=250, y=200))

s1 = "passing a string to the title using a closure_callback"
button1 = tk.Button(
    root, 
    text=s1, 
    fg = 'blue',
    command=closure_callback(s1))

s2 = "passing a string to the title using a lambda_callback"
lambda_callback = lambda: change_title(s2)
button2 = tk.Button(
    root, 
    text=s2,
    fg='blue',
    command=lambda_callback)

s3 = "passing a string to the title using a partial function"
button3 = tk.Button(
    root, 
    text=s3, 
    fg='blue',
    command=partial(on_Button4, s3))

# no need to pass an argument, will cycle through a given list of colors
button4 = tk.Button(
    root, 
    bg= "gold", 
    text="press me",
    command=change_color)

# left mouse button click action
#button4.bind('<Button-1>', change_color)

# use the pack() layout manager to position the widgets
# default is top down in the center
button1.pack(padx=100, pady=10)
button2.pack(padx=100, pady=10)
button3.pack(padx=100, pady=10)
button4.pack(padx=100, pady=10)

root.mainloop()
