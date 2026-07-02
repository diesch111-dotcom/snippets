#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" canvas_wallpaper_b64_tk101.py

use a base64 encoded string of a .gif or .png image to wallpaper a Tkinter 
canvas (handy for relatively small >2k image files)


create base64 image string with:
pick a GIF or PNG image file you have in the working directory
or give the full path,  for instance ...
import base64
img_file = "../image/tile/BG_honey.gif"
# python3
b64 = base64.encodebytes(open(img_file,"rb").read())
print("bg_honey_gif_b64='''\\\n" + b64.decode("utf8") + "'''")



tested with LinuxMint and Spyder IDE  dns(vegaseat)  19jun2026
"""

# created with Base64encGIF_py23.py
# base64 encoded GIF image string
grape_gif_b64='''\
R0lGODlhIAAgALMAAAAAAAAAgHCAkC6LV76+vvXeswD/ANzc3DLNMubm+v/6zS9PT6Ai8P8A////
/////yH5BAEAAAkALAAAAAAgACAAAAS00MlJq7046803AF3ofAYYfh8GIEvpoUZcmtOKAO5rLMva
0rYVKqX5IEq3XDAZo1GGiOhw5rtJc09cVGo7orYwYtYo3d4+DBxJWuSCAQ30+vNTGcxnOIARj3eT
YhJDQ3woDGl7foNiKBV7aYeEkHEignKFkk4ciYaImJqbkZ+PjZUjaJOElKanqJyRrJyZgSKkokOs
NYa2q7mcirC5I5FofsK6hcHHgsSgx4a9yzXK0rrV19gRADs=
'''

bg_honey_gif_b64='''\
R0lGODlhHAAuALMAAAAAAIAAAACAAICAAAAAgIAAgACAgICAgMDAwP8AAAD/AP//AAAA//8A/wD/
/////yH5BAAAAAAALAAAAAAcAC4AAwTQcCFJp3122Fq3pw81cB9JYpJmWt8XTmNLrRWKqDKSgyI9
+RIbbrVDPF6Lgc1EOyInTuLpmHOWNtHiIiu5UEmDcMu62B5N4VHa5Px60m/xCR2mrT3xYQ4+g9W1
G3d+gE1lN4RVOklAWiEpiCsYMIxAjoeUiZOQLoZ6mDWKMZ+cj6Mnoaakl5ugmqk8KU+mVF5LgGQc
XDu6Y25TtkmiWGfDsjA3ch5WZHkif7nEHIIVfEXVhtLPH3cdK9fInj9FQsIkjT07jEJF564y6hns
leg0EQA7
'''

ladybug_gif_b64='''\
R0lGODlhIAAgALMAAP///wAAADAwMP99Hf8AAP+lAP//AMopUwAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAACH5BAAAAAAALAAAAAAgACAAAwTHEMhJq714hp3lDh0GiqH2UWOVAt96pUIsBLKglWg87Dwv
4xMBj0Asxgg+XKxwLBJrxUGsI5TKnARoVHoLDp5XbNP5cwmNAqwa/aOc13ByrfKOw2UGw1SSxrb+
AWIxeXsAaX92UDQ1Nh6BdneMhQIHkHGSjYaVlmt4epmacp19YAKEoJRspKWrjBapWWGqcm1uB5tj
ok4HZa+3m5wEt5kuhpTAcb+FVL/NzspAfDHPysslMJjEIS0oLygnOMVd0SwcHeDk6errEQA7
'''

import tkinter as tk

root = tk.Tk()
root.title('wallpaper from base64 string')

#gif_image = tk.PhotoImage(data=tile_confetti_gif_b64)
gif_image = tk.PhotoImage(data=bg_honey_gif_b64)

# image width and height
iw = gif_image.width()
ih = gif_image.height() 

# canvas width and height
cw = 415
ch = 350
canvas = tk.Canvas(root, width=cw, height=ch)
canvas.pack()

# tile/wallpaper the image across the canvas
for x in range(0, cw, iw):
    for y in range(0, ch, ih):
        canvas.create_image(x, y, image=gif_image, anchor='nw')

# create a label with text and font and place inside the canvas
cosa24b = ('Comic Sans MS', 32, 'bold')
label = tk.Label(root, text='hello', font=cosa24b)
label.place(in_=canvas, x=40, y=30)

root.mainloop()