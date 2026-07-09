#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" PG_colors101.py

The PyGame GUI module can take color tuples (R, G, B) or color 
quadruples like (R, G,  B, A) having integer values from 0 to 255
for Red, Green, Blue or Alpha (transparency).  Alpha=0 is fully
transparent and Alpha=255 is not transparent (default). Pygame has
the option of naming some popular colors, but if some transparency
is needed you have to use the (R, G,  B, A) tuple!

Google Gemini is very helpful here!

in the Linux terminal type:
sudo apt-get install python3-pygame 
to get pygame installed if needed 


tested using Spyder or Sublime IDE on Linux  dns(vegaseat)  9jul2026
"""

import pygame as pg

pg.init()

# testing...
# prints a dictionary of all {name: (R, G, B, A)} pairs
#print(pg.color.THECOLORS)

# some popular pygame color tuples assigned to variables
# try a color name string and see if it works
aqua = (0, 255, 255)     # or just use 'aqua' etc.
black = (0, 0, 0)        # 'black' works too
blue = (0, 0, 255)       # 'blue'
darkgreen = (0, 100, 0)  # sweet!
gold = (255, 215, 0)     # 'gold' I like
green = (0, 255, 0)      # try 'green'
grey = (190, 190, 190)   # and 100 shades of grey
khaki = (240, 230, 140)
lime = (0, 255, 0)       
magenta = (255, 0, 255)
orange = (255, 165, 0)  
pink = (255, 192, 203)
red = (255, 0, 0)  
salmon = (250, 128, 114)
tan = (210, 180, 140)
violet = (238, 130, 238)
wheat = (245, 222, 179)
white = (255, 255, 255)  # 'white' will do
yellow = (255, 255, 0)

# create a width x height pixel display window
w = 580
h = 520
win = pg.display.set_mode((w, h))
# optional title bar caption
pg.display.set_caption('A couple of overlapping circles')
# create a white drawing canvas
canvas = pg.Surface(win.get_size())
canvas.fill('aqua')

# on the canvas draw a number of overlapping circle
# syntax ...
# draw.circle(Surface, color, pos, radius, width)
# width of 0 (default) fills the circle

# first red
center1 = (110, 300)
radius1 = 100
# give some transparancy? Hmmm
#red_t = (255, 0, 0, 0)
pg.draw.circle(canvas, red, center1, radius1, width=40)

# then of course gold
center2 = (380, 340)
radius2 = 150
pg.draw.circle(canvas, 'gold', center2, radius2, width=0)

# see if 'forestgreen' works
center3 = (260, 210)  # (x, y) position
radius3 = 200
# draw.circle(Surface, color, pos, radius, width)
# width of 0 (default) fills the circle
pg.draw.circle(canvas, 'forestgreen', center3, radius3, width=0)

# transfer the canvas to the display window at ulc (x=0, y=0)
win.blit(canvas, (0, 0))

# update the display window to show the drawing
pg.display.flip()

# event loop checks exit conditions (corner titlebar x click)
# keeps running and checks key events
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
            