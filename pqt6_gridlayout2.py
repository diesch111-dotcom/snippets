#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' pqt6_gridlayout2.py

using PyQt's QGridLayout with rowspan

addWidget(QWidget, row, column, rowSpan=1, columnSpan=1, alignment=0)
alignments are Qt.AlignLeft, Qt.AlignCenter etc.

https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGridLayout.html

rowCount()

tested with VSCodium IDE on LinuxMint  VegasEat 22aug2026
'''

from PyQt6.QtWidgets import *

class GridLayout2(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # setGeometry(x, y, width, height)
        self.setGeometry(70, 150, 350, 280)
        self.setWindowTitle('grid layout with span')

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        label = QLabel("this long text would stretch column zero!")

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        # addWidget(QWidget, row, column, rowSpan=1, columnSpan=1)
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        # span over 5 rows
        grid.addWidget(reviewEdit, 3, 1, 5, 1)
        # span over 2 culumns
        grid.addWidget(label, 9, 0, 1, 2) #, Qt.AlignLeft)

        self.setLayout(grid)
        self.resize(350, 300)  # alternate size

        print(grid.columnCount())    # 2
        print(grid.rowCount())       # 10
        print(grid.columnStretch(0)) # 0
        # itemAtPosition(row, column)
        print(grid.itemAtPosition(1, 0))
        print(title)


app = QApplication([])
qb = GridLayout2()
qb.show()
app.exec()
