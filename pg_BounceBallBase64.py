#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' PG_bounce_ball_base64.py

Bounce a red ball whose image is stored in this code as base64 text
Animate via clock = pg.time.Clock() and clock.tick()

https://www.pygame.org/docs/ref/pygame.html

If needed, in the terminal try:
sudo apt-get install python3-pygame   

tested with IDLE IDE on LinuxMint  VegasEat 15jun2026
'''

import pygame as pg
import base64

"""
# use this Python3 program to create a base64 encoded image string
# (base64 encoding produces a readable string from a binary image)
# then copy and paste the result into your pygame program ...
import base64
gif_file = "../image/ball_r.gif"
gif_bytes = open(gif_file, 'rb').read()
b64_bytes = base64.encodebytes(gif_bytes)
# decode <class 'bytes'> bytestring to string
b64_str = b64_bytes.decode("utf8")
print( "ball_red_gif64='''\\\n" + b64_str + "'''" )
"""

ball_red_gif64='''\
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
'''

# encode string to <class 'bytes'>, needed for Python3
ball_red_gif64 = ball_red_gif64.encode("utf8")

# convert back to a binary image to save to a file in the working directory
ball = base64.b64decode(ball_red_gif64)
with open("ball_r.gif","wb") as fout:
    fout.write(ball)

# initialize pygame
pg.init()

# now you can use the gif file you just saved
image_file = "ball_r.gif"

# image moves [x, y] at a time
im_dir = [2, 1]

# pygame uses an RGB color tuple
black = (0,0,0)
# screen width and height
sw = 600
sh = 480
# create a screen
screen = pg.display.set_mode((sw, sh))
# give the screen a title
pg.display.set_caption('bouncing ball (press escape to exit)')

# load the ball image file
image = pg.image.load(image_file).convert()
# get the rectangle that the image occupies
im_rect = image.get_rect()

clock = pg.time.Clock()

# the event loop also loops the animation code
while True:
    pg.event.pump()
    keyinput = pg.key.get_pressed()
    # exit on corner 'x' click or escape key press
    if keyinput[pg.K_ESCAPE] or pg.event.peek(pg.QUIT):
        # opposite of pg.init()
        pg.quit()
        raise SystemExit

    # set the move
    im_rect = im_rect.move(im_dir)
    # detect the boundaries and change directions
    # left/right boundaries are 0 to sreen width
    if im_rect.left < 0 or im_rect.right > sw:
        im_dir[0] = -im_dir[0]
    # top/bottom boundaries are 0 to screen height
    if im_rect.top < 0 or im_rect.bottom > sh:
        im_dir[1] = -im_dir[1]
    # this erases the old sreen with black
    screen.fill(black)
    # put the image on the screen
    screen.blit(image, im_rect)
    # update screen
    pg.display.flip()
    # use a frame rate of 30 to 60 to avoid flickering
    # lower tick value to slow movement
    clock.tick(40)
