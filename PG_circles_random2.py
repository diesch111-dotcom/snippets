#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' PG_circles_random2.py

Use module pygame to display random circles

vegaseat  26oct2026
'''

import pygame as pg
from random import randint

pg.init()  # optional habit

# create a (width, height) pixel screen and set its title
# size depends on your display resolution
width = 1800
height = 1000
screen = pg.display.set_mode((width, height))
pg.display.set_caption('  Circles  '*11)

# typical pygame event loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # most reliable exit on corner x click
            pg.quit()
            raise SystemExit
    # create random (r, g, b) color
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    # create random center position(x, y) for the circle
    random_pos = (randint(10, width), randint(10, height))
    # create random radius for the circle
    random_radius = randint(10, height//5)
    # create a new random circle
    pg.draw.circle(screen, random_color, random_pos, random_radius)
    # show the new circle
    pg.display.flip()  
    # wait 200 milliseconds to draw the next random circle
    pg.time.wait(200)
    
