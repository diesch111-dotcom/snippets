#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" turtle_circles_random2.py

Use Python module turtle to draw random color, random size circles
at random locations

vegaseat  15jun2026
"""

import random as rn
import turtle as tu

rn.seed()
tu.title(" CIRCLES "*12)
tu.bgcolor('wheat')
tu.pencolor('darkgreen')
colors = ['red', 'lime', 'blue', 'orange', 'green', 'navy', 'plum', 'red',
   'gold', 'white', 'tan', 'violet', 'purple', 'brown', 'olive', 'blue',
   'lavender', 'cyan', 'magenta', 'maroon', 'seagreen', 'yellow', 'tan',
   'thistle', 'tomato', 'turquoise', 'snow', 'sienna', 'salmon', 'gold']

# default pen width is 1
tu.width(3)

for k in range(100):
    # pen up
    tu.up()
    x = rn.randint(-300, 280)
    y = rn.randint(-380, 256)
    tu.goto(x, y)
    # pen down
    tu.down()
    tu.fillcolor(rn.choice(colors))
    tu.begin_fill()
    radius = rn.randrange(10, 170)
    tu.circle(radius)
    tu.end_fill()

# keep showing until window corner x is clicked
tu.done()
