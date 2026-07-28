#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt5_draw_circles1.py

draw drop style circles with PyQt5

tested with LinuxMint and SublimeText IDE   vegaseat  19jul2026
'''

# for Qt
from PyQt5.QtCore import *
# for Qpainter
from PyQt5.QtGui import *
# for QWidget, QPushButton, QLabel, QApplication etc
from PyQt5.QtWidgets import *

class DrawCircles(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(200, 200, 650, 650)
        self.setWindowTitle('Draw circles')

    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self)
        # optional
        paint.setRenderHint(QPainter.Antialiasing)
        # make a white drawing background
        paint.setBrush(Qt.white)
        paint.drawRect(event.rect())
        # for circle make the ellipse radii match
        radx = 100
        rady = 100
        # draw red circles, yellow fill
        paint.setPen(Qt.red)
        for k in range(125, 320, 10):
            center = QPoint(k, k)
            # optionally fill each circle yellow
            paint.setBrush(Qt.yellow)
            rady -= 10
            paint.drawEllipse(center, radx, rady)
        # draw blue circles, green fill
        paint.setPen(Qt.blue)
        radx = 100
        rady = 100
        for k in range(540, 455, -10):
            center = QPoint(k, k)
            # optionally fill each circle yellow
            paint.setBrush(Qt.green)
            radx -= 10
            paint.drawEllipse(center, radx, rady)

        paint.end()

app = QApplication([])
circle = DrawCircles()
circle.show()
app.exec_()
