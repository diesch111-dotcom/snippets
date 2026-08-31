#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_polygon_basic.py


tested with VSCodium IDE on LinuxMint  VegasEat 28aug2026
'''

from PyQt6.QtCore import QPoint, Qt
from PyQt6.QtGui import QBrush, QColor, QPainter, QPolygon
from PyQt6.QtWidgets import QApplication, QWidget


class Polygon(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Polygon Example")
        self.resize(400, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Define points for a 5-point star or polygon
        points = [
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

        # Create the polygon container
        polygon = QPolygon(points)

        # Set styling: outlines (Pen) and fill (Brush)
        painter.setPen(QColor("black"))
        painter.setBrush(QBrush(QColor(0, 0, 255)))

        # Draw the polygon
        painter.drawPolygon(polygon)


if __name__ == "__main__":
    app = QApplication([])
    po = Polygon()
    po.show()
    app.exec()

