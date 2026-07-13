
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" SirpinskiTriangle1.py

Draw a Sierpinski Triangle (fractal) to a set depth using PIL.
Named after Polish mathematician Waclaw Sierpinski.
It starts with an equilateral triangle, then smaller triangles are 
added by connecting to the midpoints of each of the sides.

PIL, the Python Imaging Library has image processing features.
Now called Pillow, a modern, actively maintained fork of PIL.
Colors can be given as color name strings.

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


def sierpinski_t(data, steps, update_image, k):
    '''
    calculates points for sub triangles, uses recursion for steps
    '''
    # draw triangles each step through with individual lines
    update_image.line((data[0], data[1]))
    update_image.line((data[1], data[2]))
    update_image.line((data[0], data[2]))

    # next triangle formed by connecting the midpoints of each of the sides
    x1 = (data[0][0] + data[1][0]) // 2
    y1 = (data[0][1] + data[1][1]) // 2

    x2 = (data[1][0] + data[2][0]) // 2
    y2 = (data[1][1] + data[2][1]) // 2

    x3 = (data[2][0] + data[0][0]) // 2
    y3 = (data[2][1] + data[0][1]) // 2

    # updates data in next recursion
    data2 = ((x1, y1), (x2, y2), (x3, y3))

    # loop through until step limit is reached
    k += 1
    if k <= steps:
        # the functions calls itself (recursion)
        sierpinski_t((data[0], data2[0], data2[2]), steps, update_image, k)
        sierpinski_t((data[1], data2[0], data2[1]), steps, update_image, k)
        sierpinski_t((data[2], data2[1], data2[2]), steps, update_image, k)


def draw(image):
    '''draws picture/image'''
    return ImageDraw.Draw(image)


# higher steps gives more detail
# test with values of 1 to 10
steps = 6

# the three x,y data points for the starting equilateral triangle
data = ((0, 500), (500, 500), (250, 0))

# picture canvas creation uses size tuple info given in data[1]
size = data[1]
picture = Image.new('RGB', size, color='blue')
update_image = draw(picture)

# draw the triangle and calculate next triangle corner coordinates
sierpinski_t(data, steps, update_image, 0)

"""
pillow's canvas.show()
brings up the modified image in a viewer, kind of crude, saves the image
as a usually large bitmap file (persists) and calls a .bmp viewer
"""

# better...
# save as .png .jpg .gif or .bmp file
# depending on the file extension used
# (the .jpg format gives the smallest file size)
# (the .png format gives the best color quality)
# look at the saved file with a picture viewer
filename = "PIL_SierpinskiTriangle1.png"
picture.save(filename)
print('image file {} saved'.format(filename))

# nicer...
# show image using Tkinter ...
from PIL import ImageTk
import tkinter as tk

root = tk.Tk()
# only set ULC (x, y) position of root (optional)
root.geometry("+{}+{}".format(150, 100))
root.title(filename)

# convert PIL image objects to Tkinter PhotoImage objects
tk_image1 = ImageTk.PhotoImage(picture)

# display the image on a label (auto expands to size)
label1 = tk.Label(root,image=tk_image1)
label1.pack(padx=5, pady=5)

root.mainloop()
