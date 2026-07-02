''' PG_DrawLines2.py
draw a corner pattern of lines with pygame using:
draw.line(Surface, color, start_pos, end_pos, width=1)

modified from: http://wordpress.com/tag/pygame-tutorial/

Pygame can use color (r, g, b) tuples
optional (red, green, blue, transparency)
goes from most transparent=0 to least=255 (default)

black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
olive = (128, 128, 0)
orange = (255, 165, 0)
magenta = (255, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
limegreen = (50, 205, 50)
gold = (255, 215, 0)
lavender = (230, 230, 250)
linen = (250, 240, 230)
tan = (210, 180, 140)
wheat = (245, 222, 179)

docs
https://www.pygame.org/docs/ref/pygame.html

in the LinuxMint terminal type:
sudo apt-get install python3-pygame  
to install pygame if needed


tested using the LinuxMint OS and Spyder IDE  dns(vegaseat)  19jun2026
'''

import pygame as pg

# set some color rgb tuples
black = 0, 0, 0
blue = 0, 0, 255
green = 0, 255, 0
light_blue = 173, 216, 230
olive = 128, 128, 0
orange = 255, 165, 0
magenta = 255, 0, 255 
red = 255, 0, 0
yellow = 255, 255, 0
white = 255, 255, 255

# set width and height of window/screen
w = h = 499 
screen = pg.display.set_mode((w + 1, h + 1))
pg.display.set_caption('Draw an artsy screen of lines')
# background
screen.fill(light_blue)

# experiment with size and step
size = 250
step = 20
# show some neat looking lines
for x in range(0, size+1, step):
    # pygame.draw.line(Surface, color, start_pos, end_pos, width=1)
    pg.draw.line(screen, red, (0, size-x), (x, 0), 2)
    pg.draw.line(screen, olive, (w - (size-x), 0), (w, x), 2)
    pg.draw.line(screen, blue, (w, h - (size-x)), (w-x, h), 2)
    pg.draw.line(screen, magenta, (250-x, h), (0, h-x), 3)
 
# update display
pg.display.flip()

# run event loop with exit conditions (titlebar x click)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # most reliable exit on corner x click
            pg.quit()
            raise SystemExit

