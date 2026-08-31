#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_ellipse_circle.py

center(x, y), draws circle if radius_x and radius_y are equal
otherwise ellipse
drawEllipse(center, radius_x, radius_y)

color_rand = QColor(rn.randrange(256), rn.randrange(256), rn.randrange(256))

tested with IDLE IDE on LinuxMint  VegasEat 28aug2026
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
        # create a random color (r, g, b) tuple
        self.color_rand = QColor(rn.randrange(256), rn.randrange(256),
                           rn.randrange(256))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # set center point and radius_x and radius)y
        # make radii different for an ellipse
        center = QPointF(self.width() / 2, self.height() / 2)
        radius_x = radius_y = 100.0

        # setPen() sets border line color
        painter.setPen(QColor("black"))
        # setBrush() sets fill color
        painter.setBrush(QBrush(self.color_rand))

        # Draw circle: center_x, center_y, rad_x, rad_y
        painter.drawEllipse(center, radius_x, radius_y)


if __name__ == "__main__":
    app = QApplication([])
    cr = Circle()
    cr.show()
    app.exec()


