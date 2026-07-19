#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" pqt6_Hello.py

If need be use the Linux Software Manager to install Python3-pyqt6

tested using the Spyder IDE on Linux OS  dns aka vegaseat  13jul2026
"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

def main():
    # 1. Every PyQt app must create an application object
    app = QApplication(sys.argv)
    
    # 2. Create the main window container
    window = QWidget()
    window.setWindowTitle("My First PyQt App")
    # width, height
    window.resize(300, 100)
    
    # 3. Create a layout and add a text label widget
    layout = QVBoxLayout()
    label = QLabel("Hello, World!")
    layout.addWidget(label)
    
    # 4. Set the layout on the window and display it
    window.setLayout(layout)
    window.show()
    
    # 5. Start the application's event loop and exit cleanly when done
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
