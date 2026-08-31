#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_ellipse_circle.py

PyQt is a little different then other GUIs...
it asks for the center point (x, y) coordinates and 
for the radius along the x axis or radius_x and 
the radius along the y axis or radius_y
It draws circle if radius_x and radius_y are equal
otherwise it's an ellipse
all numeric values are floats, syntax...
drawEllipse(center, radius_x, radius_y)

multiple circles via a loop could be 'artsy'

tested with VSCodium IDE on LinuxMint  VegasEat 31aug2026
'''

import random as rn
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QBrush, QColor, QPainter
from PyQt6.QtWidgets import QApplication, QWidget


class Circle(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Circle")
        self.resize(400, 400)
        # to randomize color use...
        # create random integers for red green blue values
        rn.seed()
        r = rn.randrange(256)
        g = rn.randrange(256)
        b = rn.randrange(256)
        self.color_rand = QColor(r, g, b)

    def paintEvent(self, event):
        '''QPainter triggers the paintEvent'''
        painter = QPainter(self)

        # set center point (x, y) and radius_x and radius_y
        # make radii different for an ellipse, 
        # use QPointF() for floats
        center = QPointF(self.width() / 2, self.height() / 2)
        radius_x = radius_y = 150.0

        # setPen() sets border line color
        painter.setPen(QColor("black"))
        # setBrush() sets fill color
        painter.setBrush(QBrush(self.color_rand))

        # values are floats: center point (x, y), radius_x, radius_y
        painter.drawEllipse(center, radius_x, radius_y)


if __name__ == "__main__":
    app = QApplication([])
    cr = Circle()
    cr.show()
    app.exec()

