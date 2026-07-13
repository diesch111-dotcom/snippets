#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" PIL_SirpinskiTree1.py

Draw a SirpinskiTree
Named after the Polish mathematician Waclaw Sierpinski.
PIL the Python Imaging Library has image processing features
Now called Pillow, a modern, actively maintained fork of PIL
Colors can be given as color name strings

Works seamlessly with Python's tkinter GUI

Notice:
The online C compiler at:
https://www.onlinegdb.com/online_c_compiler#
also runs Python3.  I use it on FireFox to test several computer languages.
(select Python 3 from dropdown menu in upper left corner)
For GUI fans: that Python version comes with tkinter and PIL installed!
Save the picture by clicking the right mouse button on it for a menu.
A little fickle at times on repeats.  This program happens to works okay!


On a Linux terminal use ...
sudo apt-get install python3-pillow
to install pillow if needed

Even though you install pillow, you still use the PIL namespace 
in your Python code.

tested using the Spyder IDE on Linux  dns(vegaseat)  9jul2026
"""

from PIL import Image, ImageDraw
from math import sin,cos,pi

def sierpinski_tree(iter, origin, t, r, theta, dtheta):
    """
    iter     iteration number (stop when iter == 0)
    origin   x,y coordinates of the start of the tree
    t        current trunk length
    r        factor of contraction of the trunk each iteration
    theta    current orientation
    dtheta   angle of the branch in radians
    """
    if iter == 0: 
        return []
    x0, y0 = origin
    x, y = x0+t*cos(theta), y0+t*sin(theta)
    lines = [((x0, y0),(x, y))]
    lines.extend(sierpinski_tree(iter-1,(x,y),t*r,r,theta+dtheta,dtheta))
    lines.extend(sierpinski_tree(iter-1,(x,y),t*r,r,theta-dtheta,dtheta))
    return lines


def pil_render_lines(lines, height=400, width=420):
    # create empty image to draw on
    img = Image.new("RGB", (width, height), 'wheat')
    draw = ImageDraw.Draw(img)
    for line in lines: 
        draw.line(line, (0,0,0))
    
    fname = "PIL_SirpinskiTree1.png"
    img.save(fname)
    print('{} saved'.format(fname))
    # image data
    return img

def main():
    # initial  trunk length
    t = 150
    # factor, amount to contract the trunk each iteration
    r = 0.6
    # convert degrees to radians factor
    ang2rad = pi/180.
    # initial orientation
    theta = 90.0*ang2rad
    # initial angle of the branch
    dtheta = 60.0*ang2rad
    lines = sierpinski_tree(8, (200, 0), t, r, theta, dtheta)
    # get img data
    img = pil_render_lines(lines)
    return img

if __name__ == '__main__': 
    # get image data for tk
    img = main()
    
    # show image using Tkinter ...
    from PIL import ImageTk
    import tkinter as tk

    root = tk.Tk()
    # only set ULC (x, y) corner position of the root window
    root.geometry("+{}+{}".format(150, 100))
    root.title('PIL_SirpinskiTree1')

    # convert PIL image objects to Tkinter PhotoImage objects
    tk_image1 = ImageTk.PhotoImage(img)

    # display the image on a label (auto expands to size)
    label1 = tk.Label(root,image=tk_image1)
    label1.pack(padx=5, pady=5)

    root.mainloop()
