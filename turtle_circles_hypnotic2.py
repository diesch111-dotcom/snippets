''' turtle_circles_hypnotic2.py

Use Python module turtle to draw a number of concentric circles

vegaseat  15jun2026
'''

import turtle as tu

tu.title(" HYPNOTIC? "*10)
tu.bgcolor('wheat')
tu.pencolor('darkgreen')

# default pen width is 1
tu.width(3)

for radius in range(10, 400, 10):
    # pen up
    tu.up()
    # move pen to point x, y
    # keeps the center of the circle at canvas center
    tu.goto(0, -radius)
    # pen down
    tu.down()
    tu.circle(radius)


# keep showing until window corner x is clicked
tu.done()
