#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_polygon_triangle.py

Draw a triangle using a 3 point QPolygon

Use QPolygon (integer coordinates) or
QPolygonF (floating-point coordinates)
QColor.colorNames()  gives a list of 148 predefined colors

featuring...
painter = QPainter()
painter.setRenderHint()
QPoint(x, y)
QPolygon(list of 3 points)
painter.setPen(QColor())
painter.setBrush(QColor())
painter.drawPolygon()

tested with IDLE IDE on LinuxMint  VegasEat 20aug2026
'''

from PyQt6.QtCore import QPoint, Qt
from PyQt6.QtGui import QBrush, QColor, QPainter, QPolygon
from PyQt6.QtWidgets import QApplication, QWidget


class Triangle(QWidget):

    def __init__(self):
        # inherits from Qwidget
        super().__init__()
        self.setWindowTitle("PyQt6 Triangle")
        # resize(width, height)
        self.resize(400, 400)

    def paintEvent(self, event):
        ''' QPainter sets up paintEvent()'''
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # the 3 corner coordinates  of a triangle
        top = QPoint(200, 50)
        bottom_right = QPoint(320, 300)
        bottom_left = QPoint(80, 300)

        # do the triangle via QPolygon give list of 3 corner coordinates
        triangle = QPolygon([top, bottom_right, bottom_left])

        # setPen() sets border line
        painter.setPen(QColor("black"))
        # setBrush() sets fill color
        painter.setBrush(QBrush(QColor("navy")))

        # do the triangle
        painter.drawPolygon(triangle)


if __name__ == "__main__":
    app = QApplication([])
    tr = Triangle()
    tr.show()
    # event loop...
    app.exec()


