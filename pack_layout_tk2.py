#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pack_layout_tk2.py

Looking at the Tkinter pack() layout manager

don't mix pack() and grid() in the same container widget
If you have to mix, use 2 different frames one for pack()
and one for grid()

Starting with TCL/Tk 8.6 this will be flagged as an error.

pack() defaults are side='top' and anchor='center'
fill=0, expand=0, ipadx=0, ipady=0, padx=0, pady=0
ipad is internal padding and pad is external padding
or from the center on down

Again, you can use place() and grid() or
place() and pack() layout managers together,
but not pack() and grid()

https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/shipman/

tested using the Spyder IDE on Linux  vegaseat  19jul2026
'''

import pprint
import tkinter as tk

root = tk.Tk()
root.title("The pack() layout manager")

# set the root window's height, width and x,y position
# x and y are the coordinates of the upper left corner
w = 300
h = 400
x = 50
y = 100
# use width x height + x_offset + y_offset (no spaces!)
# if geometry() is not use the frames will make space to fit root
root.geometry("{}x{}+{}+{}".format(w, h, x, y))
# or use f_string format, new in Python3.6
# root.geometry(f"{w}x{h}+{x}+{y}")

frame1 = tk.Frame(root,
                  bg='green',
                  relief='ridge',
                  border=8,
                  width=240,
                  height=200)
frame2 = tk.Frame(root,
                  bg='yellow',
                  relief='ridge',
                  border=8,
                  width=240,
                  height=200)
b1 = tk.Button(frame1, text="Button1")
b2 = tk.Button(frame1, text="Button2")
b3 = tk.Button(frame1, text="Button3")
b4 = tk.Button(frame1, text="Button4")
b5 = tk.Button(frame1, text="Button5")
b6 = tk.Button(frame1, text="Button6")
b7 = tk.Button(frame1, text="Button7")
# switching to frame2
b8 = tk.Button(frame2, text="Button8")
b9 = tk.Button(frame2, text="Button9")
lb = tk.Label(frame2, text='label1', fg='red', bg='white')  # , width=40)

# frames fill and expands along the the x axis only or both
frame1.pack(fill='x', expand='yes')
frame2.pack(fill='both', expand='yes')
# line widgets up from the top down by default
b1.pack(side='top')
# can also use 'top' and expand in horizontal x direction
b2.pack(side='top', fill='x', expand='yes')
# line widgets up from left to right
b3.pack(side='left')
# can also external pad in x and y directions
# b4.pack(side='left', padx=10, pady=30)
# or you can use a dictionary to pack (similar to b4.pack_info)
pack_dict = {'side': 'left', 'padx': 10, 'pady': 30}
b4.pack(**pack_dict)
# these will line up on top of each other left of button4
b5.pack()
b6.pack()
b7.pack()
# these are in frame2
# pack() could be replaced by grid() at this point if so desired
b8.pack(side='top', fill='x', expand='yes')
# 'e' = east or from right side of frame
b9.pack(anchor='e')
lb.pack(fill='x', expand='yes')

print('dictionary of pack info for button2:')
pack_dict = b4.pack_info()
pprint.pprint(pack_dict)
print('-'*20)
print(pack_dict['anchor'])  # center

# optional, but interesting
# get the size of the used root space (root.update is needed!)
root.update()
width = root.winfo_width()  # 195
print('width of the used root space = {} pixel'.format(width))
height = root.winfo_height()  # 243
print('height of the used root space = {} pixels'.format(height))

root.mainloop()

''' show result...
dictionary of pack info for button2:
{'anchor': 'center',
 'expand': 0,
 'fill': 'none',
 'in': <tkinter.Frame object .!frame>,
 'ipadx': 0,
 'ipady': 0,
 'padx': 10,
 'pady': 30,
 'side': 'left'}
--------------------
center
width of the used root space = 300 pixel
height of the used root space = 400 pixels
'''
