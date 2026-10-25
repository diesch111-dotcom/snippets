''' turtle_circles_fill2.py

Use Python module turtle to draw a number of concentric circles.
Move the center of each cicle slowly to the North

vegaseat  15jun2026
'''

import turtle as tu

# 15 colors
rainbow = ['navy', 'blue3', 'blue', 'darkcyan', 'cyan', 'lightGreen',
    'lime', 'yellow2', 'yellow', 'orange', 'magenta', 'red', 'red3',
    'maroon', 'moccasin']

tu.title(" RAINBOW? "*10)
# names for speed are 'fastest' (0, no delay), 'fast', (10, delay 5ms),
# 'normal' (6, delay 10ms), 'slow' (3, delay 15ms), 'slowest' (1, delay 20ms)
tu.speed('fast')
tu.pencolor('darkgreen')

width = 1100
height = 1100
# also set background color
tu.screensize(width, height, 'wheat')

# default pen width is 1
tu.width(3)

for ix, radius in enumerate(range(380, 10, -25)):
    # pen up
    tu.up()
    # move pen to circle center point x, y
    # start lower and move slowly up North
    tu.goto(0, -radius - 120 + radius/3)
    # pen down
    tu.down()
    tu.fillcolor(rainbow[ix])
    tu.begin_fill()
    tu.circle(radius)
    tu.end_fill()

# keep showing until window corner x is clicked
tu.done()
