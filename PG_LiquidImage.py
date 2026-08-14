#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' PG_LiquidImage.py

PyGame liquid effect on a single image

If needed, in the LinuxMint terminal type:
sudo apt-get install python3-pygame  

tested with Spyder IDE on LinuxMint  VegasEat 19jul2026
'''

import pygame as pg
import math

pg.init()
# set width and height of pygame window
w = 600
h = 400
screen = pg.display.set_mode((w, h), pg.HWSURFACE|pg.DOUBLEBUF)
pg.display.set_caption('Liquid animation of an image')

# load image file you have
# if not in the working folder, add full path
image_file = '../image/PythonHand2.jpg'
bitmap = pg.image.load(image_file)
# double the image size
#bitmap = pg.transform.scale2x(bitmap)

# put image and screen into the same format
if screen.get_bitsize() == 8:
    screen.set_palette(bitmap.get_palette())
else:
    bitmap = bitmap.convert()

increment = 0.0
x_list = range(0, w, 10)
y_list = range(0, h, 10)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
    increment += 0.08
    for x in x_list:
        xpos = (x + (math.sin(increment + x*0.01)*15)) + 20
        for y in y_list:
            ypos = (y + (math.sin(increment + y*0.01)*15)) + 20
            screen.blit(bitmap, (x, y), (xpos, ypos, 20, 20))
    pg.display.flip()

