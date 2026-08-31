#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_polygon_star.py

Draw a 5 pointed star using 10 corner corner coordinates

use QPolygon (integer coordinates) or
QPolygonF (floating-point coordinates)
QColor.colorNames()  gives a list of 148 predefined colors

featuring...
painter = QPainter()
painter.setRenderHint()
QPoint(x, y)
star = QPolygon(list of 10 points)
painter.setPen(QColor())
painter.setBrush(QColor())
painter.drawPolygon(star)

tested with IDLE IDE on LinuxMint  VegasEat 28aug2026
'''

from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QColor, QPainter, QPolygon
from PyQt6.QtWidgets import QApplication, QWidget


class Star(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Polygon Star")
        self.resize(400, 400)
        bgString = "QWidget { background-color: %s }"
        # for color use string #rrggbb eg. yellow --> #ffff00
        bgNavy=  bgString % QColor("navy").name()
        # set the background color of the form
        self.setStyleSheet(bgNavy)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Define points for a 5-point star polygon
        star_points = [
            QPoint(200, 50),
            QPoint(240, 150),
            QPoint(350, 150),
            QPoint(260, 210),
            QPoint(290, 310),
            QPoint(200, 250),
            QPoint(110, 310),
            QPoint(140, 210),
            QPoint(50, 150),
            QPoint(160, 150),
        ]

        # reate the polygon
        star = QPolygon(star_points)

        #setPen() sets border line
        painter.setPen(QColor("red"))
         # setBrush() sets fill color
        painter.setBrush(QColor("yellow"))

        # draw the cre<ted polygon
        painter.drawPolygon(star)


if __name__ == "__main__":
    app = QApplication([])
    sr = Star()
    sr.show()
    app.exec()
