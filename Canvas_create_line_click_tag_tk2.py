''' Canvas_create_line_tag_click_tk2.py

Draw some Tkinter canvas shapes:
4 lines and  a rectangle
Show shape names when clicked?

the trick is to create all the shapes in a function and return the functions
vars() local dictionary inverted.

docs
https://tkdocs.com/shipman/canvas.html
https://tkdocs.com/shipman/create_line.html
https://tkdocs.com/shipman/canvas-tags.html

works fine on
LinuxMint with Python3 and Python3-tk installed

tested using the Spyder IDE on Linux  dns aka vegaseat  15jul2026
'''

import tkinter as tk


def clicked(event):
    """display the clicked widgets's name"""
    name = shape_dict[cv.find_withtag('current')[0]]
    sf = 'clicked shape {}'.format(name)
    root.title(sf)

def create_shapes():
    """
    keep local dictionary vars() clean
    return of the proper dictionary from vars() is important
    assigned widget names show in shape_dict[cv.find_withtag('current')[0]]
    """
    line1 = cv.create_line(0, 10, 320, 10, fill='red', width=5, tags='click')
    line2 = cv.create_line(0, 30, 320, 30, fill='blue', width=5, tags='click')
    line3 = cv.create_line(0, 50, 320, 50, fill='green', width=5, tags='click')
    rect1 = cv.create_rectangle(50, 70, 280, 85, fill='magenta', tags='click')
    # make an apparent rectangle from an extra wide line
    line4xw = cv.create_line(50, 115, 280, 115, fill='red', width=50, tags='click')
    # reverse local dictionary vars()
    # needed for shape names in function clicked() 
    return dict((v, k) for (k, v) in vars().items())


root = tk.Tk()

cv = tk.Canvas(root, width=330, height=150, bg='white')
cv.pack()

# the shape dictionary is used by function cicked()
shape_dict = create_shapes()
# test
print(shape_dict)
# {1: 'line1', 2: 'line2', 3: 'line3', 4: 'rect1', 5: 'line4xw'}

# left mouse click = '<1>'
cv.tag_bind('click', '<1>', clicked)

# shows possible options for the tk.Canvas() widget
import pprint
pprint.pprint(cv.keys())

root.mainloop()

''' canvas options...
['background',
 'bd',
 'bg',
 'borderwidth',
 'closeenough',
 'confine',
 'cursor',
 'height',
 'highlightbackground',
 'highlightcolor',
 'highlightthickness',
 'insertbackground',
 'insertborderwidth',
 'insertofftime',
 'insertontime',
 'insertwidth',
 'offset',
 'relief',
 'scrollregion',
 'selectbackground',
 'selectborderwidth',
 'selectforeground',
 'state',
 'takefocus',
 'width',
 'xscrollcommand',
 'xscrollincrement',
 'yscrollcommand',
 'yscrollincrement']
'''