#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_Hello2.py

Applying a font to a QLabel, also apply a stylesheet for color.
could use...
from PyQt6.QtGui import QColor, QFont

eg.
QFont(family, pointSize, weight, italic)
weight options are QFont.Light=25, QFont.Normal=50, QFont.Bold=75
by default pointSize=12, weight=50, italic=False

Hurray...
Here is the 'Hello World' example with font and in color somewhat simplified
The flaw Gtk-Message we Linux folks ignore

QLabel in PyQt6 doesn't have a built-in clicked signal like QPushButton

tested with VSCodium IDE on LinuxMint  VegasEat 20aug2026
'''

import sys
# consider wildcard imports to be initially okay with pyqt
# name conflicts are limited because of the consistent 'Q' prefix of widgets
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

def main():
    app = QApplication([])
    # avoid the window, do just a label
    text = ' Hello World! '
    label = QLabel(text)
    font = QFont("Times", 44)
    label.setFont(font)
    # set the location (Upper Left Corner coordinates), size to fit
    label.move(100, 150)

    # set the foreground and background colors of the label
    # the label text is considered foreground 
    fg = "QLabel {color:red}"
    bg = "QLabel {background-color:yellow}"
    # apply with a style sheet
    label.setStyleSheet( fg+bg )
    # show your genius effort
    label.show()

    # start the application's event loop with app.exec()
    # also allow the window corner x click to exit when done
    sys.exit(app.exec())   

if __name__ == "__main__":
    main()   