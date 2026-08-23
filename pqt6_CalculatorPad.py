#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_CalculatorPad.py

using PyQt's QGridLayout to lay out the buttons for a small calculator pad

addWidget(QWidget, row, column, rowSpan=1, columnSpan=1, alignment=0)
alignments are Qt.AlignLeft, Qt.AlignCenter etc.

tested with VSCodium IDE on LinuxMint  VegasEat 22aug2026
'''

from PyQt6.QtWidgets import *


class CalculatorPad(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # setGeometry(x_pos, y_pos, width, height)
        # width, height = 1, 1 auto-fit widgets
        self.setGeometry(70, 150, 1, 1)
        self.setWindowTitle('grid layout')
        label = QLabel("Result: ")
        # optional style
        label.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Sunken)
        self.edit = QLineEdit()


        bt_names = ['Cls', 'Bck', '', 'Close',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+']

        grid = QGridLayout()

        pos = [(0, 0), (0, 1), (0, 2), (0, 3),
            (1, 0), (1, 1), (1, 2), (1, 3),
            (2, 0), (2, 1), (2, 2), (2, 3),
            (3, 0), (3, 1), (3, 2), (3, 3 ),
            (4, 0), (4, 1), (4, 2), (4, 3)]

        j = 0
        for btn in bt_names:
            button = QPushButton(btn)
            if j == 2:
                # addWidget(QWidget, row, column, rowSpan=1, columnSpan=1)
                grid.addWidget(QLabel(''), 0, 2)
            else: grid.addWidget(button, pos[j][0], pos[j][1])
            j = j + 1

        grid.addWidget(label, 5, 0)
        grid.addWidget(self.edit, 5, 1, 1, 3)

        self.setLayout(grid)


app = QApplication([])
qb = CalculatorPad()
qb.show()
app.exec()
