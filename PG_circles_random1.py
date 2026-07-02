''' PG_circles_random1.py
use module pygame to display random circles
draw.circle(Surface, color, pos, radius, width)

pg.time.wait(milliseconds)

in the LinuxMint terminal type:
sudo apt-get install python3-pygame   
to install pygame if needed

tested on LinuxMint and Spyder IDE  dns(vegaseat)  19jun2026
'''

import pygame as pg
from random import randint

pg.init()  # optional habit

# create a 640x480 pixel window/screen and set its title
width = 640
height = 480
screen = pg.display.set_mode((width, height))
pg.display.set_caption('Enjoy Pygame Random Circles')

# event loop with exit conditions (titlebar x click)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # most reliable exit on corner x click
            pg.quit()
            raise SystemExit
    # create random (r, g, b) color
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    # create random center position(x, y) for the circle
    # stay within screen dimensions
    random_pos = (randint(0, 639), randint(0, 479))
    # create random radius for the circle
    random_radius = randint(1,200)

    # create a new circle
    pg.draw.circle(screen, random_color, random_pos, random_radius)

    # show the new circle
    pg.display.flip()

    # wait 100 milliseconds to draw the next random circle
    pg.time.wait(100)
    