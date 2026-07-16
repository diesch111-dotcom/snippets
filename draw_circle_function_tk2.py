''' draw_circle_function_tk2.py

Tkinter draws a circle/oval an a cv = tk.Canvas()
for example  cv.create_oval(rect, fill='red') will be a red circle
where rect is a rectangle with given corner ULC and LRC coordinates
if it's a square a circle is drawn, otherwise an oval is drawn,
use width=0 to avoid a border

create some helper functions:
get_center(x1, y1, x2, y2)
get_square(x, y, radius)
draw_circle(center, radius, color=None, width=0) 
draw_circle2(x, y, radius, color=None, width=0) 

to animate a circle use...
cv.move(obj, xAmount, yAmount)
cv.after()
write a function call it move_circle()


using the Spyder IDE on Linux  dns aka vegaseat 4jul2026
'''

import pprint
import tkinter as tk


def move_circle():
    ''' a recursive function '''
    step_y = 1  # move along y axis only
    step_x = 0
    step_time = 25  # milliseconds delay
    # create an "orange_circle" object in main
    cv.move("orange_circle", step_x, step_y)
    x0, y0, x1, y1 = cv.bbox("orange_circle")
    canvas_height = 600
    if y1 > canvas_height: 
        return
    cv.after(step_time, move_circle)

def get_center(x1, y1, x2, y2):
    '''
    for a rectangle with ULC=(x1,y1) and LRC=(x2,y2)
    calculate the center (x,y)
    '''
    x = x1 + (x2 - x1)//2
    y = y1 + (y2 - y1)//2
    return x, y

def get_square(x, y, radius):
    '''
    given the center=(x,y) and radius
    calculate the square for the circle to fit into
    return x1, y1, x2, y2 of square's ULC=(x1,y1) and LRC=(x2,y2)
    '''
    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius
    return x1, y1, x2, y2

def draw_circle(center, radius, color=None, width=0):
    '''
    given the center point=(x,y) tuple and radius
    draw a circle on the tkinter canvas
    '''
    # to draw a circle you need to get the upper left
    # and lower right corner coordinates of a square
    x1 = center[0] - radius
    y1 = center[1] - radius
    x2 = center[0] + radius
    y2 = center[1] + radius
    square = [x1, y1, x2, y2]
    # draw a circle that fits into the square
    # if fill is given a color then the circle is filled with this color
    # width is the width of the outline, width=0 avoids any outline/border
    cv.create_oval(square, fill=color, width=width)
    # vars() contains the data dictionary of draw_circle() object
    return vars()

def draw_circle2(x, y, r, color=None, width=0):
    """
    form a bounding square using center (x,y) and radius r
    """
    ulc = x-r, y-r   # upper left corner 
    lrc = x+r, y+r   # lower right corner
    cv.create_oval(ulc, lrc, fill=color, width=width)
    # vars() contains the data dictionary of draw_circle2() object
    return vars()


# create the basic window, let's call it 'root'
root = tk.Tk()
root.title('Draw circles within a square and more...')

# create a canvas to draw on
cv = tk.Canvas(root, width=600, height=600, bg='white')
cv.grid()

# this tagged circle will be moving in function move_circle()
x4 = 500    # center x
y4 = 10     # center y
r4 = 50     # radius
square4 = get_square(x4, y4, r4)
# give the circle a tag name for reference used in cv.move()
cv.create_oval(square4, tag="orange_circle", fill='orange')
move_circle()

# draw a circle with given center (x,y) and radius
x1, y1 = 100, 100
radius1 = 65
# to draw a circle you need to get the ul and lr corner coordinates
# of a square that the circle will fit inside of
square1 = get_square(x1, y1, radius1)
# draw the circle that fits into the rect/square
# default fill is canvas bg
#cv.create_oval(rect)
circle1 = cv.create_oval(square1, fill='red')

# testing ...
# upper_left and lower_right box corners of square around circle
print(cv.coords(circle1))

# using draw_circle function with center point (x, y)
center2 = (300, 100)
radius2 = 65
circle2 = draw_circle(center2, radius2, 'blue')
# draw_circle() returns a dictionary of the circle's data
pprint.pprint(circle2)
'''
{'center': (300, 100),
 'color': 'blue',
 'radius': 65,
 'square': [235, 35, 365, 165],
 'width': 0,
 'x1': 235,
 'x2': 365,
 'y1': 35,
 'y2': 165}
'''
# optionally show the rectangle/square the circle2 fits into
# border width is in pixels
cv.create_rectangle(circle2['square'], width=2)

x3 = 220
y3 = 250
# overlapping circles form a 'drop' shape
for x in range(1, 100, 3):
    circle3 = draw_circle2(x3 - x, y3 + x, x, 'green')

color_list = ['red', 'green', 'blue', 'gold', 'purple', 'lightblue', 
              'peachpuff', 'orange', 'magenta', 'brown', 'black', 'tan']
for x in range(len(color_list)):
    # change center_x, radius and color
    draw_circle2(300+10*x, 400, radius2-4*x, color_list[x])

# tired of them squares?
x5 = 30
y5 = 500
rect = x5, y5, x5+200, y5+50
cv.create_oval(rect, fill='darkorchid')
cv.create_rectangle(rect, width=2)

root.mainloop()
