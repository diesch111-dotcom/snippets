#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" pqt6_BoxLayout.py

Use PyQt QHBoxLayout for a horizontal box layout of 3 buttons

self.

layout.addWidget(btn1, stretch=1)  # Takes 1 part space
layout.addWidget(btn2, stretch=2)  # Takes twice as much space as btn1
# sets uniform spacing (in pixels) between widgets
hbox.setSpacing(20) 
# (left, top, right, bottom) in pixels
hbox.setContentsMargins(10, 10, 20, 10)

tested with VSCodium IDE on LinuxMint  VegasEat 22aug2026
"""

import sys
# for QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication
from PyQt6.QtWidgets import *


class BoxLayout(QWidget):
    def __init__(self, parent=None):
        # QWidget is self ...
        QWidget.__init__(self, parent)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(100, 150, 320, 100)
        #self.resize(300, 150)
        self.setWindowTitle('vertical and hoorizontal box layout')

        self.ok = QPushButton("OK")
        self.cancel = QPushButton("Cancel")
        self.quit = QPushButton("Quit program")
        self.quit.clicked.connect(app.closeAllWindows)

        # horizontal layout
        hbox = QHBoxLayout()
        # hbox widgets move with window expansion horizontally
        hbox.addStretch(True)
        # add all buttons horizontally
        hbox.addWidget(self.ok)
        hbox.addWidget(self.cancel)
        hbox.addWidget(self.quit)
        # sets uniform spacing (in pixels) between widgets
        hbox.setSpacing(20) 
        # (left, top, right, bottom) in pixels
        hbox.setContentsMargins(10, 10, 20, 10)
        self.setLayout(hbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    bx = BoxLayout()
    bx.show()
    # start the application's event loop with app.exec()
    # and allow the window corner x click to exit when done
    sys.exit(app.exec())
