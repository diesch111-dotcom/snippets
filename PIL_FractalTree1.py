''' PIL_FractalTree1.py
Draw a fractal tree using PIL, again kind of artsy-fartsy!
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

from PIL import Image, ImageDraw
import math


def fractal_tree(iter, origin, t, r, theta, dtheta):
    """
    returns a list of line begin/end coordinate tuples
    iter     iteration number, stop when iter == 0
    origin   x,y coordinates of the start of this branch
    t        current trunk length
    r        factor to contract the trunk each iteration
    theta    starting orientation
    dtheta   angle of the branch
    """
    if iter == 0:
        return []
    x0, y0 = origin
    x, y = x0 + t * math.cos(theta), y0 + t * math.sin(theta)
    lines = [((x0,y0), (x,y))]
    # recursive calls
    lines.extend(fractal_tree(iter-1, (x,y), t * r, r, theta + dtheta, dtheta))
    lines.extend(fractal_tree(iter-1, (x,y), t * r, r, theta - dtheta, dtheta))
    return lines

def draw_lines(lines, width=420, height=350):
    """draw and return the fractal tree image"""
    # create an empty image to draw on
    image1 = Image.new("RGB", (width, height), 'wheat')
    draw = ImageDraw.Draw(image1)
    for line in lines:
        draw.line(line, 'black')
        #print line  # test
    return image1

# test the functions ...
if __name__ == '__main__':
    # angle to radian factor
    ang2rad = math.pi/180.0
    # experiment with number of iterations (try 4 to 16)
    iter = 13
    # experiment with trunk length (try 100)
    t = 120
    # experiment with factor to contract the trunk each iteration (try 0.65)
    r = 0.65
    # starting orientation (initial 90 deg)
    theta = 90.0 * ang2rad
    # experiment with angle of the branch (try 60 deg)
    dtheta = 60.0 * ang2rad
    # center of top
    origin = (200, 0)
    
    lines = fractal_tree(iter, origin, t, r, theta, dtheta)
    
    # change width and height as needed ...
    width = 400
    height = 300
    image1 = draw_lines(lines, width, height)
    
    """
    pillow's canvas.show()
    brings up the modified image in a viewer, kind of crude, saves the image
    as a usually large bitmap file (persists) and calls a .bmp viewer
    """
    
    # better...
    # save as .png .jpg .gif or .bmp file
    # depending on the file extension used
    # (the .jpg format may give the smallest file size)
    # (the .png format gives the best color quality)
    # look at the saved file with a picture viewer
    filename = 'PIL_FractalTree1.png'
    image1.save(filename)
    print('file {} saved'.format(filename))

    # nicer...
    # show image using Tkinter ...
    import tkinter as tk
    from PIL import ImageTk

    root = tk.Tk()
    root.title(filename)
    # only set ULC (x, y) corner position of the root window
    root.geometry("+{}+{}".format(150, 100))

    # convert PIL image objects to Tkinter PhotoImage objects
    tk_image1 = ImageTk.PhotoImage(image1)

    # display the image on a label (auto expands to size)
    label1 = tk.Label(root,image=tk_image1)
    label1.pack(padx=5, pady=5)

    root.mainloop()

    