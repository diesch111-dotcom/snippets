#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_Painter_drawRect.py

Explore the PyQt GUI to draw rectangles in different colors
there are a number of ways colors can be specified

most flexible ...
QColor(r, g, b, alpha=255)
where r, g, b are red, green, blue values as integers 0 to 255
alpha is the transparency value (0 --> most transparent)

QColor(0, 0, 0) --> black
or use "#rrggbb" string
QColor("#ff0000") --> red

148 color names are available ...
QColor('black')

fill colors are set with the brush
perimeter colors are set with the pen

featuring...
qp = QPainter()
qp.begin()
qp.setPen(QColor("color-name"))
qp.setBrush(QColor("color-name"))
qp.drawRect(int x, int y, int width, int height)
qp.end()

tested with VSCodium IDE on LinuxMint  VegasEat 28aug2026
'''

# for QPainter, QColor, 
from PyQt6.QtGui import *
# for bread and butter items QWidget, QPushButton, QLabel etc
from PyQt6.QtWidgets import *


class MyWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        # setGeometry(x_pos, y_pos, width, height)
        # upper left corner coordinates (x_pos, y_pos)
        self.setGeometry(300, 300, 370, 100)
        self.setWindowTitle('Colors set with brush and pen')

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

        # can use QColor(r, g, b) with values 0 to 255
        # qp.setBrush(QColor(255, 0, 0)) or
        qp.setBrush(QColor("#ff0000"))
        # drawRect(int x, int y, int width, int height)
        # upper left corner coordinates (x, y)
        qp.drawRect(10, 15, 90, 60)

        # use a preset named color
        qp.setBrush(QColor('green'))
        qp.drawRect(160, 25, 90, 60)

        # this rectangle will overlap the previous one
        # you can give it some transparency alpha 0 to 255
        # QColor(int r, int g, int b, int alpha=255)
        qp.setBrush(QColor(0, 0, 255, 100))
        qp.drawRect(130, 15, 90, 60)

        # some colors can be given as preset color strings
        qp.setBrush(QColor('yellow'))
        qp.drawRect(265, 25, 90, 60)


app = QApplication([])
# forms the drawing canvas
wind = MyWindow()
wind.show()
# run the application event loop
app.exec()
