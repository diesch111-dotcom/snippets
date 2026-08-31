#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_polygon_hexagon.py

Draw a standard hexagon (all sides equal) with QPolygonF(float-points)
Calculate the 6 corner points using trigonometry, math.cos() and math.sin()
based on a center point and a radius

tested with IDLE IDE on LinuxMint  VegasEat 29aug2026
'''

import math
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QBrush, QColor, QPainter, QPolygonF
from PyQt6.QtWidgets import QApplication, QWidget


class Hexagon(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Hexagon")
        self.resize(400, 400)
        bgString = "QWidget { background-color: %s }"
        # for color use string #rrggbb eg. yellow --> #ffff00
        bgNavy=  bgString % QColor("wheat").name()
        # set the background color of the form
        self.setStyleSheet(bgNavy)

    def get_hexagon_points(self, center_x, center_y, radius):
        """generates 6 corners for a regular hexagon"""
        # list of corner coordinates
        points = []
        for n in range(6):
            # angle is in radians (60 degrees = pi / 3)
            # subtracting pi/2 or math.radians(30) rotates it
            # with one flat-top up
            angle = math.radians(60 * n)
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            points.append(QPointF(x, y))
        return points

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Center and radius parameters
        center_x = self.width() / 2
        center_y = self.height() / 2
        radius = 120

        # Calculate vertices and construct QPolygonF
        vertices = self.get_hexagon_points(center_x, center_y, radius)
        hexagon = QPolygonF(vertices)

        # Set styling (Border and Fill)
        painter.setPen(QColor("navy"))
        painter.setBrush(QBrush(QColor("olive")))

        # Draw the hexagon
        painter.drawPolygon(hexagon)


if __name__ == "__main__":
    app = QApplication([])
    hx = Hexagon()
    hx.show()
    app.exec()
