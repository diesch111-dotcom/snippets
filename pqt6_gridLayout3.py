#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_gridLayout3.py

explore multiple QFrame() in a QGridLayout() using
rowspan and columnspan

addWidget(QWidget, row, column, rowSpan=1, columnSpan=1, alignment=0)
alignments are Qt.AlignLeft, Qt.AlignCenter etc.

https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGridLayout.html

tested with VSCodium IDE on LinuxMint  VegasEat 22aug2026
'''

# for QColor
from PyQt5.QtGui import *
# for QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication
from PyQt6.QtWidgets import *


class MyFrame(QWidget):
    def __init__(self, title, width, height, parent=None):
        # create the window (this will be instance self)
        QWidget.__init__(self, parent)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(70, 150, width, height)
        self.setWindowTitle(title)
        self.makeFrame()

    def makeFrame(self):
        frame1 = QFrame(self)
        frame1.setLineWidth(3)
        frame1.setFrameStyle(QFrame.Shape.Box|QFrame.Shadow.Sunken)
        bg = "QFrame {background-color:yellow}"
        # apply with a style sheet
        frame1.setStyleSheet(bg)

        frame2 = QFrame(self)
        frame2.setLineWidth(3)
        frame2.setFrameStyle(QFrame.Shape.Box|QFrame.Shadow.Sunken)
        bg2 = "QFrame {background-color:lime}"
        # apply with a style sheet
        frame2.setStyleSheet(bg2)

        frame3 = QFrame(self)
        frame3.setLineWidth(3)
        frame3.setFrameStyle(QFrame.Shape.Box|QFrame.Shadow.Sunken)
        # optionally add color with QColor(r, g, b)
        # name() function returns the color in required format "#RRGGBB"
        lavender = QColor(230, 230, 250).name()
        # stay with required % specifier
        sf = "QFrame { background-color: %s }" % lavender
        # frame3 background will be lavender
        frame3.setStyleSheet(sf)

        grid = QGridLayout()
        grid.setSpacing(10)
        # addWidget(QWidget, row, column, rowSpan=1, columnSpan=1)
        # span 2 rows and 1 column each
        grid.addWidget(frame1, 1, 1, 2, 1)
        grid.addWidget(frame2, 1, 2, 2, 1)
        # span 1 row and 2 columns
        # note that you occupy row 3 now
        # since a rowSpan of 2 was used before that
        grid.addWidget(frame3, 3, 1, 1, 2)
        # finish the layout
        self.setLayout(grid)

        # put a label on frame1 and frame3
        label1 = QLabel("rowspan=2  columnspan=1", frame1)
        # move(x,y) within the frame, coordinates in pixels
        label1.move(10, 10)
        label3 = QLabel("rowspan=1  columnspan=2", frame3)
        label3.move(10, 10)


# create the Qt Application
app = QApplication([])
title = "3 frames in a grid layout"
width = 600
height = 300
frame = MyFrame(title, width, height)
frame.show()
# run the main Qt event loop
app.exec()