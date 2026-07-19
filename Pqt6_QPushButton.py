#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" pqt6_QPushButton.py

QPushButton click signal

If need be use the Linux Software Manager to install Python3-pyqt6

tested ++ using the Spyder IDE on Linux OS  dns aka vegaseat  13jul2026
"""

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt6.QtWidgets import QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Signals & Slots Demo")
        self.resize(300, 150)

        # 1. Create the widgets
        self.label = QLabel("Click the button to change me!")
        # Center the text inside the label
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        
        self.button = QPushButton("Click Me!")

        # 2. Connect the Signal to the Slot
        # Signal: self.button.clicked
        # Slot:   self.on_button_click
        self.button.clicked.connect(self.on_button_click)

        # 3. Arrange the widgets in a vertical layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # 4. Set the layout inside a central widget container
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # 5. Define the Slot (the Python function that reacts to the signal)
    def on_button_click(self):
        if self.label.text() == "Click the button to change me!":
            self.label.setText("Success! The text has changed. 🎉")
            self.button.setText("Reset")
        else:
            self.label.setText("Click the button to change me!")
            self.button.setText("Click Me!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()