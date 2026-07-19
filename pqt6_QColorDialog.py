#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" pqt6_QColorDialog.py

An easy way to pick colors for your GUI project


If need be use use the Linux Software Manager to install Python3-pyqt6

tested ++ using the Spyder IDE on Linux OS  dns aka vegaseat  13jul2026
"""

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton 
from PyQt6.QtWidgets import QVBoxLayout, QColorDialog
from PyQt6.QtGui import QPalette
import sys


class ColorPickerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QColorDialog Example")
        self.resize(400, 300)

        # Main Layout Setup
        layout = QVBoxLayout()
        
        # Create a button that triggers our picker method
        self.button = QPushButton("Pick a Background Color 🎨")
        self.button.clicked.connect(self.choose_color)
        layout.addWidget(self.button)

        # Set up container
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def choose_color(self):
        # 1. Get the current background color to use as the default starting 
        # selection
        current_color = self.palette().color(QPalette.ColorRole.Window)

        # 2. Open the Dialog 
        # Arguments: (initial_color, parent_window, dialog_title)
        color = QColorDialog.getColor(current_color, self, 
                                      "Select App Background")

        # 3. Check if the returned color is valid
        # If the user clicks "Cancel", .isValid() returns False
        if color.isValid():
            # Use a palette modification to update the window color 
            # programmatically
            palette = self.palette()
            palette.setColor(QPalette.ColorRole.Window, color)
            self.setPalette(palette)
            self.setAutoFillBackground(True)
            
            # Print the Hex code to the console just for reference
            print(f"User picked: {color.name()}")  # eg. #ffbe6f

def main():
    app = QApplication(sys.argv)
    window = ColorPickerApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()