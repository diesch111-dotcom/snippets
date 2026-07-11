''' PIL_tk_canvas_together_tk2.py

Create a circle with 24 segments using tk arc and PIL piesclice
use Tkinter to draw the arcs on a tk canvas to display
use PIL simultaneously to draw on a PIL canvas to save that drawing

color:
PIL takes some named colors like 'red' or 'yellow'
or color hex strings #rrggbb like '#ff0000' for red
or color rgbtuples like (255, 0, 0) for red
tkinter takes color names or hex strings

# convert rgb tuple to hex string
rgb_color = (r, g, b)
hex_color = '#' + "".join("{:02x}".format(v) for v in rgb_color)

On a Linux terminal use ...
sudo apt-get install python3-pillow
to install pillow if needed

Even though you install pillow, you still use the PIL namespace 
in your Python code.

tested using the Spyder IDE on Linux  dns(vegaseat)  11jul2026
'''

from PIL import Image, ImageDraw
import tkinter as tk

root = tk.Tk()
root.title("draw 24 arcs to make a full circle")

w = 420
h = 420
cv_tk = tk.Canvas(width=w, height=h, bg='white')
cv_tk.pack(expand='yes', fill='both')

img_pil = Image.new("RGB", (w, h), 'white')
cv_pil = ImageDraw.Draw(img_pil)

# canvas.create_arc ( x0, y0, x1, y1, option, ... )
# start = starting angle for the slice in degrees
# starts at 3 o'clock position and goes counter clockwise
# extent = width of the slice in degrees
# xy are the ULC/LRC corner coordinates of a box the arc fits in
xy = (20, 20, 400, 400)
# full circle 24 * 15 = 360
for start in range(0, 359, 15):
    # to show...
    # note: tkinter goes counter clockwise from start
    cv_tk.create_arc(xy, start=start, extent=15, fill="lime")
    # to save to file...
    # simultaneously draw a 'pieslice' arc with PIL
    # note: PIL goes clockwise from start
    cv_pil.pieslice(xy, start, start+15, fill='lime', outline='black')

# PIL images can be saved as .png .jpg .gif or .bmp files
# using the file extension
filename = "arc_circle1.jpg"
# save the PIL image
img_pil.save(filename)
print('image file {} saved'.format(filename))

root.mainloop()
