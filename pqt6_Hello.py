#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" pqt6_Hello.py

Using the VSCodium terminal to install pyqt6, if you don't have it...
python -m pip install pyqt6
...Successfully installed PyQt6-Qt6-6.11.1 PyQt6-sip-13.12.0 pyqt6-6.11.0

alas, a VSCodium message...
Gtk-Message: 17:47:16.163: Failed to load module "xapp-gtk3-module"
I was told to accept this harmless flaw due to Linux, simply ignore it!

Imports are a pain unless you simplify your life with wildcards '*'
Looks like a lot of code for such a simple thing! Bare with me, it gets better!
We still need to study and add color and a nice font!

QLabel in PyQt6 doesn't have a built-in clicked signal like QPushButton

tested with VSCodium IDE on LinuxMint  VegasEat 21aug2026
"""

import sys
# consider wildcard imports to be initially okay with pyqt
# name conflicts are limited because of the consistent 'Q' prefix of widgets
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

def main():
    # every PyQt app must create an application object
    app = QApplication(sys.argv)
    
    # create the main window 
    window = QWidget()
    # give it a title 
    window.setWindowTitle("Hello...")
    # set the location (Upper Left Corner coordinates) and size
    # setGeometry(x_pos, y_pos, width, height)
    window.setGeometry(100, 150, 300, 220)
    
    # create a simple layout and add a label widget
    layout = QVBoxLayout()
    # the infamous hello
    label = QLabel("Hello, World!")
    layout.addWidget(label)
    
    # set the layout in the window and show your genius effort
    window.setLayout(layout)
    window.show()
    
    # start the application's event loop with app.exec()
    # also allow the window corner x click to exit when done
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
