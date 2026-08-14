#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' PG_MoirePatterns2.py

Create Moire patterns using Python module pygame 
Draws closely spaced and shifted circles that create
an interference pattern often seen in silk textiles.

docs
https://www.pygame.org/docs/ref/pygame.html

Need to install pygame?
In the LinuxMint terminal try:
sudo apt-get install python3-pygame  

tested with Spyder IDE on LinuxMint  VegasEat 19jul2026l
'''

import pygame as pg
import random
import math

#screen width, height, diagonal
width = 500
height = 500
diag = math.sqrt(width**2 + height**2)

# colors in r,g,b values 0 to 255
white = 255, 255, 255
color = 46, 139, 87  # seagreen

screen = pg.display.set_mode((width, height))
pg.display.set_caption("Moire Patterns")
screen.fill(white)

# pos, xMov, yMov, spacing values
circles = []
for i in range(3):
    pos = [random.randint(0, width-1), random.randint(0, height-1)]
    xMov = random.randint(1, 3)
    yMov = random.randint(1, 3)
    spacing = random.randint(3, 3)
    circles.append([pos, xMov, yMov, spacing])

clock = pg.time.Clock()
# exit on escape or window corner x click
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # most reliable exit on x click
            pg.quit()
            raise SystemExit
        elif event.type == pg.KEYDOWN:
            # optional exit with escape key
            if event.key == pg.K_ESCAPE:
                pg.quit()
                raise SystemExit
    screen.fill(white)
    for c in circles:
        r = c[3]
        while r < diag:
            # draw.circle(Surface, color, pos, radius, width=0)
            pg.draw.circle(screen, color, c[0], r, 1)
            r += c[3]
    pg.display.flip()
    clock.tick(20)
    for c in circles:
        c[0][0] += c[1]
        if c[0][0] < 0 or c[0][0] >= width:
            c[1] *= -1
            c[0][0] += c[1]
        c[0][1] += c[2]
        if c[0][1] < 0 or c[0][1] >= height:
            c[2] *= -1
            c[0][1] += c[2]
            
