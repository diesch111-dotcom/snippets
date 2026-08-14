#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' PG_SW_Interference.py

Fancy pygame graphics creating soothing interference patterns.
How would you like that as a wallpaper in you room?
I have seen similarly wild stuff on casino floor covers!

Need pygame installed?
in the LnuxMint terminal type:
sudo apt-get install python3-pygame  

tested with IDLE IDE on LinuxMint  VegasEat 19jul2026
'''

import pygame as pg
import math

pg.init()

# width and height of screen
w = 640
h = 580
# pg.display.set_mode(size, [flags, [depth]]) -> Surface
screen = pg.display.set_mode((w, h), pg.DOUBLEBUF, 32)
pg.display.set_caption('just a moment ...')

# pg.surfarray.array3d(Surface) -> Array
pixels = pg.surfarray.pixels3d(screen)
width = len(pixels)-1
height = len(pixels[0])-1

# modify these values for different patterns ...
# (integer size gives triangle pattern)
size = 50.0       # 50.0
slant1 = 1.7      # 1.7
slant2 = 1.5      # 1.5
melt = 0.1        # 0.1

for y in range(height):
    for x in range(width):
        z1 = math.sin(x/size*slant1*math.pi)
        z2 = math.sin((x/3+y)/size*slant2*math.pi)
        z3 = math.sin(y/size*melt*math.pi)
        z = abs(z1+z2+z3)*255
        # build the image array
        pixels[x,y] = (z, z/4, z*4)

# now the 3D image will show
pg.display.update()
pg.display.set_caption('Interference patterns anyone?')

# the event loop ...
# look into events and specify an exit action
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()  # opposite of pg.init()
            raise SystemExit
