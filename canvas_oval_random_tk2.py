""" canvas_oval_random_tk2.py

The canvas.create_oval() method is used to draw circles and ellipses
coordinates of an imaginary bounding box (rectangle that encloses the oval)
or use a helper function to calulate center and radius of a circle

Tkinter can use a number of named colors (not case sensitive) like
red, green, blue, white, black, tan, pink, yellow, magenta, lightblue
lightgreen, moccasin, peachpuff, orange, grey, purple, brown
also (light=1 to dark=4) hues of colors like
red1, red2, red3, red4   etc.

tk has also color format hex "#rrggbb" for instance:
azure = '#f0ffff'
beige = '#f5f5dc'
bisque = '#ffe4c4'
chocolate = '#d2691e'
gainsboro = '#dcdcdc'
gold = '#ffd700'
thistle = '#d8bfd8'

Tkinter uses the #rrggbb hex format
PIL uses the (r, g, b) tuple format and #rrggbb hex format 

eg.
widget.after(delay_ms, callback, *args)
or just
widget.after(delay_ms)
widgt.update()

tested with LinuxMint and Spyder IDE  dns(vegaseat)  19jun2026
"""

import tkinter as tk
from random import randint

# Set up the main window and canvas
root = tk.Tk()
root.title("tkinter canvas.create_oval() example")
# set the root window's height, width and x,y position
# x,y are the upper left corner ULC coordinates 
# in pixels
w = 640
h = 480
x = 50
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry(f"{w}x{h}+{x}+{y}")


def create_circle_center(canvas, x, y, r, **kwargs):
    """draws a circle using center (x, y) and radius r"""
    return canvas.create_oval(x - r, y - r, x + r, y + r, **kwargs)

canvas = tk.Canvas(root, width=w, height=h, bg="white")
canvas.pack()

while True:
    # create random (r, g, b) color
    #random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    #f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
    random_color = \
    f"#{randint(0, 255):02x}{randint(0, 255):02x}{randint(0, 255):02x}"
    
    # create random center position(x, y) for the circle
    # stay within screen dimensions
    random_x = (randint(0, 639))
    random_y = (randint(0, 639))
    #random_pos = (randint(0, 639), randint(0, 479))
    # create random radius for the circle
    random_radius = randint(1,200)
    # draws a circle centered at (200, 250) with a radius of 50
    create_circle_center(canvas, random_x, random_y, random_radius, 
                         fill=random_color, width=4)
    canvas.after(200)
    canvas.update()

root.mainloop()