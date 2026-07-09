''' PIL_spokes1.py

Draw a 'fractal' ball using PIL, kind of artsy-fartsy!
Print them out and hang them on your Mother in Law's wall!
PIL the Python Imaging Library has image processing features
Now called Pillow, a modern, actively maintained fork of PIL
Colors can be given as color name strings or color tuples.

Works seamlessly with Python's tkinter GUI

this code adopted from:
http://www.math.union.edu/research/fractaltrees/

On a Linux terminal use ...
sudo apt-get install python3-pillow
to install pillow if needed

Even though you install pillow, you still use the PIL namespace 
in your Python code.

tested using the Spyder IDE on Linux  dns(vegaseat)  9jul2026
'''

#import os
#import time
from PIL import Image, ImageDraw
from math import sin, cos


def draw_spokes(width, height, n):
    # create an empty image to draw on
    image1 = Image.new("RGB", (width, height), 'yellow')
    draw = ImageDraw.Draw(image1)
    # accumulate the triangle drawings
    for spokes in range(3, n+3):
        radians = 360 / (spokes * 57.29578)
        for x in range(spokes):
            for y in range(spokes):
                draw.line((((int)(sin(y * radians) * 225 + 300), 
                            (int)(cos(y * radians) * 145 + 170)),
                    ((int)(sin(x * radians) * 225 + 300), 
                     (int)(cos(x * radians) * 145 + 170))), 'black')
    return image1


# test drive thia thing ...
if __name__ == '__main__':
    
    # change width and height as needed ...
    width = 600
    height = 350
    # number of triangles, use 1 to 16 ...
    n = 9
    image1 = draw_spokes(width, height, n)
    
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
    # actually these .png files are denser then .jpg
    # look at the saved file with a picture viewer
    filename = "pil_spokes1.png"
    image1.save(filename)
    print("{} saved".format(filename))
    
    # nicer...
    # show image using Tkinter ...
    from PIL import ImageTk
    import tkinter as tk

    root = tk.Tk()
    # only set ULC (x, y) corner position of the root window
    root.geometry("+{}+{}".format(150, 100))
    root.title(filename)

    # convert PIL image objects to Tkinter PhotoImage objects
    tk_image1 = ImageTk.PhotoImage(image1)

    # display the image on a label (auto expands to size)
    label1 = tk.Label(root,image=tk_image1)
    label1.pack(padx=5, pady=5)

    root.mainloop() 
