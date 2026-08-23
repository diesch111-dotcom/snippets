#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_GridDemo.py

explore multiple QFrame() in a QGridLayout() using
rowspan and columnspan

addWidget(QWidget, row, column, rowSpan=1, columnSpan=1, alignment=0)
alignments are Qt.AlignLeft, Qt.AlignCenter etc.

https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGridLayout.html

# ways to import pyqt6...
from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, 
    QLabel, QLineEdit, QTextEdit, QPushButton
)
from PyQt6.QtCore import Qt

tested with VSCodium IDE on LinuxMint  VegasEat 22aug2026
'''

import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, 
    QLabel, QLineEdit, QTextEdit, QPushButton
)
from PyQt6.QtCore import Qt

class GridDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        # Row 0: Name (Label + Input)
        layout.addWidget(QLabel("Name:"), 0, 0)
        layout.addWidget(QLineEdit(), 0, 1)

        # Row 1: Email (Label + Input)
        layout.addWidget(QLabel("Email:"), 1, 0)
        layout.addWidget(QLineEdit(), 1, 1)

        # Row 2: Bio (Label + Text Area spanning 1 row, 2 columns)
        layout.addWidget(QLabel("Bio:"), 2, 0)
        layout.addWidget(QTextEdit(), 3, 0, 1, 2)  # Row 3, Col 0, Span 1 Row, Span 2 Cols

        # Row 4: Submit button (aligned right)
        submit_btn = QPushButton("Submit")
        layout.addWidget(submit_btn, 4, 1, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)
        self.setWindowTitle("PyQt6 QGridLayout Example")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GridDemo()
    window.show()
    sys.exit(app.exec())