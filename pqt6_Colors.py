#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_Colors.py

set colors for PyQT, can use some names, color tuples(r,g,b) or hexstrings

needs...
from PyQt6.QtGui import QColor

QColor(r, g, b, alpha=255)
where r, g, b are red, green, blue values as integers 0 to 255
alpha is the transparency value (0 --> most transparent)

Pen and Brush set drawing and fill colors
a color can be selected via ...
r,g,b values 0 - 255
red = QColor(255, 0, 0)
green = QColor("#00ff00")
needs
from PyQt6.QtCore import Qt
predefined Global Color Enum...
red = QColor(Qt.GlobalColor.red)

(try a predefined color name)
QColor("colorName").name()
eg.
QColor("navy").name()    = #000080
QColor(255, 0, 0).name() = #ff0000
QColor.colorNames()      # list of 148 predefined colors

tested with Spyder IDE on LinuxMint  VegasEat 20aug2026
'''

# wildcard imports are okay since the 'Q' prefix limits collision conflicts
from PyQt6.QtGui import QColor
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class MyFrame(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(70, 150, 350, 300)
        self.setWindowTitle("paintEvent creates a canvas")
        self.set_colors()

    def paintEvent(self, event):
        """paintEvent is a preset event method of self"""
        # form the canvas to draw on
        painter = QPainter()
        painter.begin(self)
        # optional, changed in pqt6
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # use the brush for background
        painter.setBrush(QBrush(self.orange))
        # values have to be integer values, so use '//'
        # drawRect(x, y, width, height), where ulc = x, y
        x, y, width, height = eval(str(event.rect())[18:]) 
        painter.drawRect(x, y, width, height//2)

        painter.setBrush(QBrush(self.trans_yellow))
        painter.drawRect(x+10, y+10, width -20, height//2 - 20)

        painter.setBrush(QBrush(self.yellow))
        painter.drawRect(x, y+height//2, width, height//2)

        painter.end()

    def set_colors(self):
        """set some colors"""
        # color uses red, green, blue values (0 to 255)
        self.red = QColor(255, 0, 0)
        # or QColor("red")
        self.green = QColor(0, 255, 0)
        # or QColor("green")
        self.blue = QColor(0, 0, 255)
        # or QColor("blue")
        self.black =  QColor(0, 0, 0)
        self.bisque = QColor(255, 228, 196)
        self.brown = QColor(165, 42, 42)
        self.dark_green = QColor(0, 100, 0)
        self.navy = QColor(0, 0, 128)
        self.orange = QColor(255, 165, 0)
        self.plum = QColor(221, 160, 221)
        self.pale_green = QColor(152, 251, 152)
        self.yellow = QColor(255, 255, 0)
        # transparent color setting alpha to eg. 80
        self.trans_yellow = QColor(255, 255, 0, 80)
        self.white = QColor(255, 255, 255)
        # show the rgb values of a given color, test ...
        self.lavender = QColor(230, 230, 250)
        print(self.lavender.red())    # 230
        print(self.lavender.green())  # 230
        print(self.lavender.blue())   # 250


app =  QApplication([])
frame = MyFrame()
frame.show()
app.exec()

''' QColor.colorNames() ...
['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque',
'black', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblu
e', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson',
 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'dark
grey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid',
 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'dar
kslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray'
, 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia',
 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow',
 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavend
er', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'l
ightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'ligh
tpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'light
slategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'mage
nta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple'
, 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', '
mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajow
hite', 'navy', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid',
 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', '
peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown',
'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sie
nna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'sprin
ggreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'transparent', 'turquo
ise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen']
'''