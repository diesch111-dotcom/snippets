#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_Painter_drawRect.py

Explore the PyQt GUI to draw rectangles in different colors
there are a number of ways colors can be specified

most flexible ...
QColor(r, g, b, alpha=255)
where r, g, b are red, green, blue values as integers 0 to 255
alpha is the transparency value 0 to 255 (0 is most transparent)

color the most descriptive way, 148 color names are available ...
QColor('black')

fill colors are set with the brush
perimeter (outline) colors are set with the pen

featuring...
qp = QPainter()
qp.begin()
qp.setPen(QColor("color-name"))
qp.setBrush(QColor("color-name"))
qp.drawRect(int x, int y, int width, int height)
qp.end()

tested with VSCodium IDE on LinuxMint  VegasEat 31aug2026
'''

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication


class Canvas(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        # QWidget or 'self' is the canvas to draw on...
        # setGeometry(x_pos, y_pos, width, height)
        # upper left corner coordinates (x_pos, y_pos)
        self.setGeometry(300, 300, 370, 100)
        self.setWindowTitle('One overlapping rectangle has transparency')

    def paintEvent(self, e):
        '''
        the method paintEvent() is called automatically
        the QPainter class does all the low-level drawing
        coded between its methods begin() and end()
        '''
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):
        '''use QPainter (instance qp) methods to do drawings'''

        # there are 148 preset named colors
        # QPen(color, width, style)
        qp.setPen(QColor('black'))

        qp.setBrush(QColor("red"))
        # drawRect(int x, int y, int width, int height)
        # upper left corner coordinates (x, y)
        qp.drawRect(10, 15, 90, 60)

        qp.setBrush(QColor('green'))
        qp.drawRect(130, 15, 90, 60)

        # this rectangle will overlap the previous one
        # so give it some transparency alpha 0 to 255
        # 0 is most transparent, 255 is not transparent (default)
        # QColor(int r, int g, int b, int alpha=255)
        r = 0
        g = 0
        b = 255 
        alpha = 130
        qp.setBrush(QColor(r, g, b, alpha))
        qp.drawRect(160, 25, 90, 60)

        qp.setBrush(QColor('yellow'))
        qp.drawRect(265, 15, 90, 60)


app = QApplication([])
# form the drawing canvas
cv = Canvas()
cv.show()
# run the application event loop
app.exec()

